#!/usr/bin/env python3
"""Make the AI judge happy (make.fun bounty ai-happy-01), v2.

Writes one image to /output/entry.png by copying the image this
repository holds (happy.jpg) — a photorealistic laughing child with
a bunch of colorful balloons and confetti in golden-hour sunlight.
Deterministic: no network, no randomness, the same bytes on every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "happy.jpg")
OUTPUT_PATH = "/output/entry.png"


def digest(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    shutil.copyfile(SOURCE, tmp_path)
    assert digest(SOURCE) == digest(tmp_path), "output differs from source"
    os.replace(tmp_path, OUTPUT_PATH)
    print("wrote", OUTPUT_PATH, digest(OUTPUT_PATH))


if __name__ == "__main__":
    main()
