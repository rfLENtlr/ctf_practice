bytes = [0x59, 0x1e, 0x23, 0x20, 0x20, 0x2f, 0x20, 0x04, 0x2b, 0x2d, 0x36, 0x75, 0x35, 0x7f, 0x1a, 0x44, 0x07, 0x36, 0x50, 0x6d, 0x03, 0x5a, 0x17, 0x11, 0x36, 0x2b, 0x47, 0x04, 0x01, 0x09, 0x3c, 0x15, 0x38, 0x0a, 0x41]
c = b'00000000000000002e8ba2e8ba2e8ba3'
xor_bytes = [0x57, 0x65, 0x6c, 0x63, 0x6f, 0x6d, 0x65, 0x20, 0x74, 0x6f, 0x20, 0x53, 0x45, 0x43, 0x43, 0x4f, 0x4e, 0x20, 0x32, 0x30, 0x32, 0x32]
flag = ""
for i in range(35):
    A = (i * int(c, 16) >> 64) & 0b1111111111111111111111111111111111111111111111111111111111111100
    A = A * 2 + int(i/22) * 3
    B = i + A * (-2)
    flag += chr(bytes[i] ^ xor_bytes[B])

print(flag)