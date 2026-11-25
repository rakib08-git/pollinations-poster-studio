#!/usr/bin/env python3
"""Generate a poster image with the Pollinations image API.

Usage:
    POLLINATIONS_API_KEY=... python3 make_poster.py "prompt" output.png [model]
"""

import os
import sys
import urllib.parse
import urllib.request

DEFAULT_MODEL = "black-forest-labs/flux.1-schnell"
BASE = "https://gen.pollinations.ai/image/"


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    prompt, out = sys.argv[1], sys.argv[2]
    model = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_MODEL
    key = os.environ.get("POLLINATIONS_API_KEY")
    if not key:
        print("Set POLLINATIONS_API_KEY first (your own Pollinations key).")
        return 2
    url = BASE + urllib.parse.quote(prompt) + "?model=" + urllib.parse.quote(model)
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {key}", "User-Agent": "poster-studio/1.0"},
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = resp.read()
    with open(out, "wb") as fh:
        fh.write(data)
    print(f"saved {out} ({len(data)} bytes, model {model})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
