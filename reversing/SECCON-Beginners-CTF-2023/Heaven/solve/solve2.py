def str_to_hex(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

# 0x20 ~ 0x7e の文字列を暗号化したバイト列
hex_string = "d6eee087ef3f6c2d4e78b6ae51fad3b2fdf2768a3d5058d0427c10665c4821cf49cce24fc8d404e4f72901fcb475ce9b60dd132cd588479581e5c76792f093340d2b636aedcbe82f4c1f5e9d0be7055da857be06e6ec59bdc1dcc4c95a7f9f"

# 0x20 ~ 0x7e
ascii_chars = [chr(i) for i in range(0x20, 0x7F)]

# 対応表 (hex : ascii の辞書)
hex_to_ascii = dict(zip(str_to_hex(hex_string), ascii_chars))

# フラグを暗号化したバイト列
encrypted_flag = "6ae6e83d63c90bed34a8be8a0bfd3ded34f25034ec508ae8ec0b7f"

print("".join(hex_to_ascii.get(encrypted_flag[i:i+2]) for i in range(0, len(encrypted_flag), 2)))