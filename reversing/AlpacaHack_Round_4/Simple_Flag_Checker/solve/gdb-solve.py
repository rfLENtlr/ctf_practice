# gdb -x solve.py
import gdb

BINDIR = "."
BIN = "checker"
INPUT = "./in.txt"
BREAK = ["0x555555555a2f", "0x555555555a5f"]

flag = "!"*0x31
i = 0
# flag = "Alpaca{h4sh_4lgor1thm_1s_b!!!!!!!!!!!!!!!!!!!!!!!"
# i = 26

def run():
    with open(INPUT, "w") as f:
        f.write(flag)
    gdb.execute('run < {}'.format(INPUT))

def change_flag(_flag, c):
    _flag_list = list(_flag)
    _flag_list[i] = c
    _flag = ''.join(_flag_list)

    return _flag

gdb.execute('file {}/{}'.format(BINDIR, BIN))
[gdb.execute('b *{}'.format(x)) for x in BREAK]
run()

while i != 0x31:
    c = flag[i]
    for _ in range(i):
        gdb.execute('continue')
    r = int(gdb.parse_and_eval("$rax").format_string(), 16)
    if(r != 0):
        c = chr(ord(c)+1)
        flag = change_flag(flag, c)
        run()
        continue

    i += 1
    run()

gdb.execute('continue')
print(f"flag: {flag}")
gdb.execute('quit')
