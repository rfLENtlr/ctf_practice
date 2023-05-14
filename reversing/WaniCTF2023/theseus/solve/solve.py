flag = "FLAGmlEAfh.i`,f_N)r?W^c$kx"
flag_ascii = []


for j in flag:
    flag_ascii.append(ord(j))

flag = ""
for i in range(0,26):
    k = 0
    if (3 < i):
        k = (i* 0xb) % 0xf
    flag += chr(flag_ascii[i] + k)

print(flag)