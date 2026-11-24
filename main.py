"""Loading Screen Gold: a one-line tip for a stressed developer and their AI agent.

Writes the entry line to /output/entry.txt (UTF-8, single line, 108 chars).
"""

import os

ENTRY = "Tip: the build is not stuck. Your agent is just quietly Googling the error message you already pasted twice."
# Single line, 108 characters: short enough to read at a glance on a loading screen.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
