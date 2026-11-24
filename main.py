"""One Line of Earned Pride — entry.

Writes the single line to entry.txt (in MAKEFUN_OUTPUT_DIR when set,
otherwise ./output) and prints it. Standard library only.
"""

import os

LINE = (
    "He quietly stitched his own name into the shoes he'd wear to his "
    "daughter's wedding \u2014 after forty years of mending strangers' shoes."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
