from encoding_utils import get_encoding_range
from encoding_utils import get_hex_format
import os


def get_file_path(encoding_name: str, result_folder: str) -> str:
    os.makedirs(result_folder, exist_ok=True)
    return os.path.join(result_folder, f"{encoding_name}.tbl")


def check_escape(chr: str, escape_code: str, value, escape_value: str) -> str:
    if chr == escape_code:
        value = value.rstrip("\n")
        return f"/{value}{escape_value}"
    return value


def create_table(
    encoding: str, size: int, output: str, escape_code: str, escape_value: str
) -> bool:
    print("creating table...")
    with open(get_file_path(encoding, output), "w", encoding="utf-8") as file:
        encoding_range = get_encoding_range(encoding)
        if size == 0:
            hex_format = get_hex_format(encoding_range)
        else:
            hex_format = size
        if escape_code == "00":
            file.write(f"/{str(0)*hex_format}={escape_value}")
        if escape_code.__len__() < hex_format:
            escape_code = f"{str(0)*(hex_format-escape_code.__len__())}{escape_code}"
        for i in range(32, encoding_range):
            char = chr(i)
            hex_value = format(i, f"0{hex_format}X")
            value = check_escape(
                hex_value, escape_code, f"{hex_value}={char}\n", escape_value
            )
            try:
                file.write(value)
            except UnicodeEncodeError:
                pass
    print(f"created {encoding}.tbl")
    return True
