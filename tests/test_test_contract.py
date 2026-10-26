import json
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/test_contract.py'


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git('init')
        self.git('config', 'user.email', 'test@example.invalid')
        self.git('config', 'user.name', 'Contract test')
        self.git('config', 'core.autocrlf', 'false')
        (self.root / 'tests').mkdir()
        self.write('tests/test.txt', 'approved\n')
        self.write('app.txt', 'baseline\n')
        self.write('.gitignore', '*.ignored\n')
        self.git('add', '.')
        self.git('commit', '-m', 'RED')
        self.base = self.git('rev-parse', 'HEAD').strip()
        self.run_tool('seal', '--path', 'tests', '--output', 'contract.json')
        self.contract_hash = hashlib.sha256((self.root / 'contract.json').read_bytes()).hexdigest()

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.root, stderr=subprocess.PIPE).decode()

    def write(self, name, value):
        (self.root / name).write_text(value, encoding='utf-8')

    def run_tool(self, *args, ok=True):
        result = subprocess.run([sys.executable, str(SCRIPT), *args, '--base', self.base], cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0 if ok else 1, result.stdout + result.stderr)

    def verify(self, ok=True):
        self.run_tool('verify', '--manifest', 'contract.json', '--contract-sha256', self.contract_hash, ok=ok)

    def test_implementation_can_change_and_commit(self):
        self.write('app.txt', 'implementation\n')
        self.verify()
        self.git('add', 'app.txt')
        self.git('commit', '-m', 'GREEN')
        self.verify()

    def test_modified_deleted_added_ignored(self):
        for change in ('modify', 'delete', 'add', 'ignored'):
            with self.subTest(change=change):
                if change == 'modify':
                    self.write('tests/test.txt', 'changed\n')
                elif change == 'delete':
                    (self.root / 'tests/test.txt').unlink()
                else:
                    self.write('tests/new.' + ('ignored' if change == 'ignored' else 'txt'), 'new')
                self.verify(ok=False)
                self.git('checkout', '--', 'tests')
                for name in ('tests/new.txt', 'tests/new.ignored'):
                    (self.root / name).unlink(missing_ok=True)

    def test_staged_change_even_with_restored_disk(self):
        self.write('tests/test.txt', 'changed\n')
        self.git('add', 'tests/test.txt')
        self.write('tests/test.txt', 'approved\n')
        self.verify(ok=False)

    def test_manifest_tampering(self):
        manifest = json.loads((self.root / 'contract.json').read_text())
        manifest['files'] = {}
        self.write('contract.json', json.dumps(manifest))
        self.verify(ok=False)

    def test_wrong_baseline(self):
        self.base = '0' * 40
        self.verify(ok=False)

    def test_no_overwrite(self):
        self.run_tool('seal', '--path', 'tests', '--output', 'contract.json', ok=False)

    def test_path_list_tampering(self):
        manifest = json.loads((self.root / 'contract.json').read_text())
        manifest['paths'] = ['tests/test.txt']
        self.write('contract.json', json.dumps(manifest))
        self.verify(ok=False)

    def test_executable_mode_change_in_index(self):
        self.git('update-index', '--chmod=+x', 'tests/test.txt')
        self.verify(ok=False)

    def test_seal_rejects_dirty_implementation(self):
        self.write('app.txt', 'unfinished implementation')
        self.run_tool('seal', '--path', 'tests', '--output', 'other.json', ok=False)

    def test_unsafe_path(self):
        self.run_tool('seal', '--path', '../tests', '--output', 'other.json', ok=False)


if __name__ == '__main__':
    unittest.main()
