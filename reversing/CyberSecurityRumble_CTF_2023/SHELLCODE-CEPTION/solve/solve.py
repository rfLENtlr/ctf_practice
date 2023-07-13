s = 0x0212133a3175222a282f261e702f2272313570712f1e22752f1e23241e752f2f2e38702f263c
byte_list = []
while s > 0:
    byte = s & 0xFF
    byte_list.append(byte)
    s >>= 8

byte_list.reverse()

flag = "".join(chr(l ^ 0x41) for l in byte_list)

print(flag)