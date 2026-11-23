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
    python3 main.py /tmp/out/entry.png
    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py

An optional first argument names the output file outright; without one
the MAKEFUN_OUTPUT_DIR/OUTPUT_DIR environment variable (a directory) is
honoured, falling back to /output/entry.png. After writing, the program
reads the output back and checks its SHA-256 against the bundled bytes,
failing loudly instead of silently shipping a corrupt copy.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLED = HERE / "entry.png"


def output_path(argv) -> Path:
    """Where the image goes.

    Precedence: an explicit argv path (a file, or a directory to put
    entry.png in), then the kit's MAKEFUN_OUTPUT_DIR / OUTPUT_DIR
    environment variable (a directory), then /output/entry.png.
    """
    if len(argv) > 1:
        given = Path(argv[1])
        # An existing directory, or a suffix-less path, names the
        # directory to put entry.png in; anything else is the file.
        if given.is_dir() or not given.suffix:
            return given / "entry.png"
        return given
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value) / "entry.png"
    return Path("/output/entry.png")


def main(argv) -> int:
    if len(argv) > 2:
        print("usage: python3 main.py [output-path]", file=sys.stderr)
        return 2
    if not BUNDLED.is_file():
        print(f"bundled image missing: {BUNDLED}", file=sys.stderr)
        return 1
    source = BUNDLED.read_bytes()
    source_hash = hashlib.sha256(source).hexdigest()
    out = output_path(argv)
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED, out)
    written = out.read_bytes()
    written_hash = hashlib.sha256(written).hexdigest()
    if written_hash != source_hash:
        print(
            f"output verification failed: {out} "
            f"sha256={written_hash}, expected {source_hash}",
            file=sys.stderr,
        )
        return 1
    print(
        f"wrote {out} ({len(written)} bytes, "
        f"sha256={written_hash}, verified)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
