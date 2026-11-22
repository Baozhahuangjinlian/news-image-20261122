"""Entry program for the news-image-20261122 bounty.

The front page itself (entry.png) was drawn offline from the day's
verified stories and ships in this repository. This program only
carries it to the grader's output directory, unchanged.

It is deterministic by construction: the same file goes out on every
run, so two runs always write identical bytes.
"""
import hashlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        raise SystemExit("entry.png is not a PNG file")
    if data[12:16] != b"IHDR":
        raise SystemExit("entry.png has no IHDR chunk")
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds 1 MiB")
    target = out_dir / "entry.png"
    target.write_bytes(data)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
