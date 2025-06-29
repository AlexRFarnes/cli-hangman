import sys
from pathlib import Path
from string import ascii_letters


def main():
    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])

    word_list = sorted(
        {
            word.lower()
            for word in in_path.read_text(encoding="utf-8").split()
            if all(letter in ascii_letters for letter in word) and len(word) > 3
        },
        key=lambda word: (len(word), word),
    )
    out_path.write_text("\n".join(word_list))


if __name__ == "__main__":
    main()
