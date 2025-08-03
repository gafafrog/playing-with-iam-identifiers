'''
引数で受け取った文字列をBase32でデコードして、
その結果出てきたビットを配列をそのまま出力する。
'''
import sys

BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
DECODE_MAP = {char: index for index, char in enumerate(BASE32_ALPHABET)}


def base32_to_bit_array(b32_string):
    bit_string = ""
    for char in b32_string.upper():
        if char in DECODE_MAP:
            value = DECODE_MAP[char]
            bit_string += format(value, '05b')
    return bit_string


if __name__ == '__main__':
    iam_id_part = sys.argv[1]
    bit_array = base32_to_bit_array(iam_id_part)

    print(f"Base32文字列: {iam_id_part}")
    print(f"ビット配列: {bit_array}")
