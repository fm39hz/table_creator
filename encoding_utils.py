from codecs import IncrementalEncoder
import math
import encodings
import sys


def get_encoding_range(encoding_name: str) -> int:
    encoder = IncrementalEncoder()
    try:
        codec_info = encodings.search_function(encoding_name)
        if codec_info:
            encoder = codec_info.incrementalencoder()

    except AttributeError:
        print(
            f"Encoding '{encoding_name}' not found or does not support incremental encoding."
        )
        sys.exit(1)

    start = 0
    end = 0x110000

    for i in range(end):
        try:
            encoder.encode(chr(i))
            start = i
            break
        except UnicodeEncodeError:
            continue

    for i in range(end - 1, start, -1):
        try:
            encoder.encode(chr(i))
            end = i + 1
            break
        except UnicodeEncodeError:
            continue

    return end


def get_hex_format(max_value) -> int:
    return math.ceil(math.log(max_value, 16))
