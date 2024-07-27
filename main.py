import argparse
from table_creator import create_table


def args_init() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a file with character encodings."
    )
    parser.add_argument(
        "-e",
        "--encoding",
        type=str,
        help="Encoding name",
    )
    parser.add_argument(
        "-s",
        "--size",
        type=int,
        help="Bit size of the encoding",
        default=0,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output folder",
        default="result",
    )
    parser.add_argument(
        "-c",
        "--code",
        type=str,
        help="Escape code",
        default="00",
    )
    parser.add_argument(
        "-v",
        "--value",
        type=str,
        help="Escape value",
        default="[END]",
    )
    return parser.parse_args()


def main() -> None:
    args = args_init()
    encoding_name = args.encoding.lower()
    size = args.size
    output_folder = args.output
    escape_code = args.code
    escape_value = args.value
    if size < 0 or size > 8 or size % 2 == 1:
        print("invalid size")
        exit()
    create_table(
        encoding_name,
        size,
        output_folder,
        escape_code,
        f"{escape_value.rstrip("\n")}\n",
    )


if __name__ == "__main__":
    main()
