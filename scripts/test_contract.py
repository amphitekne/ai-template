"""Verify an approved Git test baseline against index and disk. Python 3 + Git."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def git(*args):
    return subprocess.check_output(['git', *args], stderr=subprocess.PIPE)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def protected(name, paths):
    return any(name == p or name.startswith(p + '/') for p in paths)


def normalize(paths):
    if not isinstance(paths, list) or not paths:
        raise ValueError('At least one protected path is required')
    result = []
    for name in paths:
        if not isinstance(name, str) or '\\' in name:
            raise ValueError('Use repository-relative forward-slash paths')
        if name.startswith('/') or ':' in name or any(p in ('', '.', '..', '.git') for p in name.split('/')):
            raise ValueError('Unsafe protected path: ' + name)
        result.append(name)
    return sorted(set(result))


def snapshot(base, paths, index=False):
    records = git('ls-files', '--stage', '-z') if index else git('ls-tree', '-r', '-z', base)
    result = {}
    for record in records.split(b'\0'):
        if not record:
            continue
        meta, raw_name = record.split(b'\t', 1)
        name = os.fsdecode(raw_name)
        if not protected(name, paths):
            continue
        mode, kind, oid = meta.decode().split() if not index else (None, None, None)
        if index:
            mode, oid, stage = meta.decode().split()
            if stage != '0':
                raise ValueError('Unmerged protected path: ' + name)
        if mode not in ('100644', '100755', '120000'):
            raise ValueError('Unsupported protected entry: ' + name)
        result[name] = {'mode': mode, 'sha256': digest(git('cat-file', 'blob', oid))}
    return result


def disk_snapshot(paths, expected):
    names = set()
    for name in paths:
        path = Path(name)
        # Never follow a symlink in a protected path's ancestors.
        if any(parent.is_symlink() for parent in path.parents):
            raise ValueError('Symlink ancestor: ' + name)
        if path.is_symlink() or path.is_file():
            names.add(name)
        elif path.is_dir():
            for root, dirs, files in os.walk(path, followlinks=False):
                for item in dirs[:]:
                    child = Path(root, item)
                    if child.is_symlink():
                        names.add(child.as_posix())
                        dirs.remove(item)
                names.update(Path(root, item).as_posix() for item in files)
    result = {}
    for name in names:
        path = Path(name)
        if path.is_symlink():
            data, mode = os.fsencode(os.readlink(path)), '120000'
        else:
            # Git's index is authoritative for executable modes on Windows.
            mode = expected.get(name, {}).get('mode', '100644') if os.name == 'nt' else ('100755' if path.stat().st_mode & 0o111 else '100644')
            data = path.read_bytes()
        result[name] = {'mode': mode, 'sha256': digest(data)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    seal = sub.add_parser('seal')
    seal.add_argument('--path', action='append', required=True)
    seal.add_argument('--output', required=True)
    verify = sub.add_parser('verify')
    verify.add_argument('--manifest', required=True)
    verify.add_argument('--contract-sha256', required=True, help='Manifest digest recorded at approval sealing')
    for command in (seal, verify):
        command.add_argument('--base', required=True, help='Independently recorded full RED commit hash')
    args = parser.parse_args()
    try:
        os.chdir(os.fsdecode(git('rev-parse', '--show-toplevel')).strip())
        base = args.base
        if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', base):
            raise ValueError('A full commit hash is required')
        if git('rev-parse', base + '^{commit}').decode().strip() != base:
            raise ValueError('Baseline must identify a commit')
        git('merge-base', '--is-ancestor', base, 'HEAD')
        if args.action == 'seal':
            paths = normalize(args.path)
            if git('rev-parse', 'HEAD').decode().strip() != base:
                raise ValueError('Seal only at the RED commit')
            git('diff', '--exit-code', base, '--')
            git('diff', '--cached', '--exit-code', base, '--')
            manifest = {'version': 1, 'base': base, 'paths': paths, 'files': snapshot(base, paths)}
            output = Path(args.output)
            if output.exists():
                raise ValueError('Refusing to overwrite an existing contract')
        else:
            manifest_bytes = Path(args.manifest).read_bytes()
            if digest(manifest_bytes) != args.contract_sha256:
                raise ValueError('Manifest digest mismatch')
            manifest = json.loads(manifest_bytes)
            paths = normalize(manifest['paths'])
            if manifest['version'] != 1 or manifest['base'] != base:
                raise ValueError('Contract baseline/version mismatch')
        expected = snapshot(base, paths)
        if not expected:
            raise ValueError('Contract must include committed test resources')
        if manifest['files'] != expected:
            raise ValueError('Manifest differs from approved Git baseline')
        if snapshot(base, paths, index=True) != expected:
            raise ValueError('Protected index differs from approved baseline')
        if disk_snapshot(paths, expected) != expected:
            raise ValueError('Protected disk content differs from approved baseline')
        if args.action == 'seal':
            relative = output.resolve().relative_to(Path.cwd()).as_posix()
            if protected(relative, paths):
                raise ValueError('Manifest must be outside protected paths')
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
            print('Record independently: --contract-sha256 ' + digest(output.read_bytes()))
        print('Test contract verified: ' + base)
        return 0
    except (ValueError, KeyError, TypeError, OSError, subprocess.CalledProcessError) as error:
        print('BLOCKED: ' + str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
