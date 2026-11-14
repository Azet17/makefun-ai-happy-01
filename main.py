#!/usr/bin/env python3
"""Make the AI judge happy (make.fun bounty ai-happy-01).

Writes one image to /output/entry.png by copying the image this
repository holds (happy.jpg). The image is a bright, joyful illustration
of a smiling girl with flowers, a rainbow and sunshine.

Deterministic: no network, no randomness, the same bytes on every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "happy.jpg")
OUTPUT_PATH = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT_PATH)


if __name__ == "__main__":
    main()
