# My solution for Simple_Flag_Checker

問題の概略、静的解析の内容、動的解析の方針については[こっちのwriteup](./writeup.md)見てください。(サボりじゃないです。向こうの解説がすばらしいんです。)僕はradare２使わないでgdbをpythonで自動化して解いたのでそのコード置いておきます。

```py
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
```

`in.txt`というファイルを予め作っておいて、こいつから入力を渡すようにします。ファイル作らないで直接値を渡す方法がよくわからなかったんでこうなっています。あとはもう一個のwriteupと同じく`0x1a2f`(gdbだとgdb側が用意するエミュレータ上の仮想メモリアドレスになるため`0x555555555a2f`)にブレークポイントを置いて、`memcmp`の比較結果が0以外なら正しくないので変数`flag`の値をasciiコード上の次の値に書き換えて、再度実行します。この時ちゃんと`in.txt`に変更加えるの忘れないようにしましょう。0なら正しいので変数`flag`の値そのままで`in.txt`も書き換えず、i+1して続きを総当りします。

ちなみにブレークポイントが２個貼ってあるのは入力値がFLAG以外である可能性を考えて、FLAGが出力される際の値を読み出してやろうと思ったからです。まぁ入力がFLAGだったので必要ないんですが。コメントアウトはそのへんでなぜがエラって落ちていたので、面倒くさくなってそのへんからリスタートするために使ったものです。もう一回やってここで落ちるかは試していません。ただの運かも。

実行結果
```sh
~~
flag: Alpaca{h4sh_4lgor1thm_1s_b4s3d_0n_MD5_4nd_keccak}
```

これミスってたら実行ロールバックして値書き換えて再実行とか出来ないのかな。なんかできた気がしますけど、忘れました。