'''
引数で受け取った文字列をBase32でデコードして、
その結果出てきたビットを配列から、開始位置を一つずつ変えずつ12桁の整数を探す。

2^39 < 999,999,999,999 < 2^40 なので、12桁の整数を表現するには40ビット必要。
'''
import sys

BASE32_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
DECODE_MAP = {char: index for index, char in enumerate(BASE32_ALPHABET)}


def base32_to_bit_array(b32_string):
    '''
    Base32文字列をビット配列（文字列）に変換する
    '''
    bit_string = ""
    for char in b32_string.upper():
        if char in DECODE_MAP:
            value = DECODE_MAP[char]
            bit_string += format(value, '05b')
    return bit_string


def find_12_digits(bit_array, looking_for=None):
    '''
    開始位置を一つずつずらしつつ、配列の中で連続した40ビットを整数にして出力する。
    '''
    for shift in range(len(bit_array) - 40):
        # 開始位置をずらし、40ビット分を切り出す
        bit_chunk = bit_array[shift : shift + 40]

        # 切り出したビットの塊を整数に変換
        candidate = int(bit_chunk, 2)

        candidate_as_str = '{:0>12}'.format(str(candidate)[:12])
        found = " <== Found!!" if candidate_as_str == looking_for else ""
        print(f"開始 {shift:2d} bit目: {candidate_as_str}{found}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("エラー: 解析するIDを引数として渡してください。")
        sys.exit(1)


    iam_id_part = sys.argv[1]
    looking_for = sys.argv[2] if len(sys.argv) > 2 else None
    bit_array = base32_to_bit_array(iam_id_part)
    print(f"Base32文字列: {iam_id_part}")
    print(f"ビット配列: {bit_array}")

    find_12_digits(bit_array, looking_for)
