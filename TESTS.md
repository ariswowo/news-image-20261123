# Verification notes

Checked locally on 23 November 2026, before pushing or submitting.
All numbers below are local checks only. This competition has no local
grade: the server grades every entry, and the result shows in the
entry's status after submission.

## The image gate

- `entry.png` is a PNG, 1024 x 1024 pixels.
- Size: 1,044,620 bytes, under the 1 MiB cap (1,048,576 bytes).
- The page names the day — "MONDAY, 23 NOVEMBER 2026" — in the
  masthead, and all five headlines are legible (checked by reading the
  rendered image).

## Determinism

`main.py` was run twice into two different output directories:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
```

Both runs wrote 1,044,620 bytes with the same SHA-256:

```
9aac776c6d4f9e77bad08b4457ac1b7dc0d01b595909c137b5fc329882571439
```

The bundled `entry.png` has the same hash. Two runs write identical
bytes, as the bounty requires.

## Kit check (official pre-submit checks)

Run from the unpacked kit:

```sh
MAKEFUN_OFFLINE=1 node cli/makefun.mjs check --kit . \
  --repo ~/workspace/makefun/news-image-20261123 --worktree
```

Result: **4 passed, 1 failed, 14 skipped, 5 checked at submission.**

Passed:

- `competition_open` — the competition is open until 2026-11-25T00:00:00Z.
- `snapshot` — 5 files, 1,052,472 bytes, within the intake caps.
- `license_osi` — LICENSE declares SPDX-License-Identifier: MIT.
- `entrypoint` — `main.py` at the root selects Python 3.13, which the
  competition accepts.

Failed:

- `transcripts_present` — no transcript bundle was supplied to the
  check. This is expected at this stage: the bundle is built when the
  entry is submitted. The remaining transcript checks were skipped for
  the same reason (no sessions to read).

Checked at submission (need the pushed public repo first):

- `repo_public`, `repo_owner`, `repo_created_after_open`,
  `commit_in_repo`, `duplicate_snapshot`.

## Still to do (not part of this local build)

1. Create the public GitHub repository (after the competition opened)
   and push this commit.
2. Bundle the agent sessions that built this entry and submit with
   the transcripts before 2026-11-25T00:00:00Z.
