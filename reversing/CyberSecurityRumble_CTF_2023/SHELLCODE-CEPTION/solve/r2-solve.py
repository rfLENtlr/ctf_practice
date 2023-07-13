import r2pipe

BINDIR = "/path/to/shellcode-ceptionのディレクトリ"
BIN = "shellcode-ception"

# [call rdx] - [vaddr]
offset1 = 0x559fa96031ef - 0x559fa9603070
# [mov edx, eax] - [call rdx]
offset2 =  0x559faa23c063 - 0x559faa23c000

r2 = r2pipe.open(BINDIR + "/" + BIN)
r2.cmd("aaa")
r2.cmd("doo")

# break at [call rdx]
break_call_rdx = hex(r2.cmdj("iej")[0]['vaddr'] + offset1)
r2.cmd("db {}".format(break_call_rdx))
r2.cmd("dc")
rdx = int(r2.cmd("dr rdx"), 16)

# break at [mov edx, eax]
break_eax = hex(rdx + offset2)
r2.cmd("db {}".format(break_eax))

flag = ""
for i in range(0x26):
    r2.cmd("dc")
    res = r2.cmd("dr eax")
    flag += chr(int(res, 16))

print(flag)