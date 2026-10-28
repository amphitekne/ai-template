---
name: capture
disable-model-invocation: true
description: Save a future idea, improvement or deferred detail in a lightweight ideas inbox without investigating, planning or implementing it; not for accepting backlog work or resolving current blockers.
---

# Capture

Run only when explicitly invoked by the human. Never activate another skill automatically; suggest the next skill and wait for the human to invoke it.

Capture means remembering a possibility, not accepting a requirement. Preserve the current story's scope, plan, tests, approvals and workflow position.

## Save the idea

1. Use the repository's existing ideas inbox if configured; otherwise use `docs/ideas.md` at the intended Git root. Resolve the root only when ambiguous, especially with independent nested repositories. Create the file only on the first actual capture, headed `# Ideas` with a short note that entries are unaccepted possibilities. Do not create an empty inbox in advance.
2. Read only the inbox and the context supplied by the human. Do not research feasibility, inspect implementation, select a stack, estimate, prioritize, write criteria, run tests or design a solution. Ask only if the note cannot be understood or its destination is ambiguous; incomplete technical detail is acceptable.
3. Add a stable unused ID such as `I-001`, a short title, and one or two sentences preserving the user's intent. Include a package/story/source reference only if supplied or already known. Do not invent context or turn suggestions into confirmed requirements. Mark the entry Pending. Use the existing inbox format when present; do not introduce required dates, categories or metadata.
4. Immediately before saving, reread the file and append without replacing other entries; choose the next unused ID from the current contents. If a near-duplicate exists, mention it and preserve any distinct information without silently discarding or rewriting prior notes. Do not renumber entries. Concurrent chats must serialize inbox writes; if the file changes during editing, reread and retry the append rather than overwrite another capture.

Edit only the ideas inbox. Never stage or commit files, change backlog/story status, modify project rules, touch protected contract paths, start environments or message another chat. If the inbox is protected by an active test contract, do not write it: return the note in chat for later capture and explain the conflict. Other active code changes do not need cleanup or tests for this documentation-only append.

## Hand back control

Confirm briefly with the idea ID and file location, stating that it does not change the active story. Do not automatically invoke backlog, story or pair. If capture temporarily interrupted an already invoked skill in this chat, resume its pending step only when the human requested continuation; approvals still require their own explicit evidence. In a separate ideas chat, finish after capture rather than attempting to continue the implementation chat.

If the note explicitly identifies a blocker, invalid approved tests or an urgent risk affecting current work, flag that it must be brought to the active pair chat now; do not silently treat it as harmless future scope or assume another chat has received the warning. A request to fix the issue belongs to the active implementation workflow, not capture.

Pending ideas are reviewed through a later explicit backlog invocation. Keep them unaccepted until the navigator decides; see the [workflow](../../../docs/workflow.md#capture-without-changing-scope).
