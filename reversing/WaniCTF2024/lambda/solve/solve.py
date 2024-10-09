# solve.py
correct_flag_encrypted = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'

corect_flag = '_'.join(chr(int(c, 36) + 10) for c in correct_flag_encrypted.split('_'))

xor = lambda _xor_flag : '_'.join(chr(123 ^ ord(c)) for c in _xor_flag.split('_') )
sub_3 = lambda _sub_3_flag : '_'.join(chr(ord(c) + 3) for c in _sub_3_flag.split('_'))
sub_4 = lambda _sub_4_flag : ''.join(chr(ord(c) - 12)  for c in _sub_4_flag.split('_'))

print(sub_4(sub_3(xor(corect_flag))))