import argparse
from pathlib import Path

import pypdf


def main() -> None:
    parser = argparse.ArgumentParser(description="merge multiple pdfs")
    parser.add_argument("--infile", required=True, nargs="*")
    parser.add_argument("--outfile", required=True, type=Path)
    args = parser.parse_args()

    merger = pypdf.PdfMerger()
    for file in args.infile:
        merger.append(file)
    with open(args.outfile, "wb") as file:
        merger.write(file)


if __name__ == "__main__":
    main()
