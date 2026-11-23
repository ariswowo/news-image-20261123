#!/usr/bin/env python3
"""make.fun bounty news-image-20261123: "Sum up 23 November's world news in one image".

The entry image is a newspaper front page for Monday 23 November 2026,
bundled in this repository as entry.png (1024 x 1024, PNG, under 1 MiB).
NEWS.md lists the five stories on the page and where each was reported.

This program uses only the Python standard library. It needs no network,
reads no clock and uses no randomness: it copies the bundled bytes to
/output/entry.png, so two runs always write byte-identical output. That is
the approach the bounty itself names: "the simplest program copies an
image the repository holds".

Run it:
    python3 main.py
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"


def output_dir() -> Path:
    """Where the image goes: the kit's variable first, then the fallback."""
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    if not BUNDLED.is_file():
        print(f"bundled image missing: {BUNDLED}", file=sys.stderr)
        return 1
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.png"
    shutil.copyfile(BUNDLED, out)
    data = out.read_bytes()
    print(
        f"wrote {out} ({len(data)} bytes, "
        f"sha256={hashlib.sha256(data).hexdigest()})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
