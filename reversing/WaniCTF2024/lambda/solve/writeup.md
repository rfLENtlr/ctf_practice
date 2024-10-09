# My solution for lambda

とりあえずlambda.pyの中身を確認してみることに、、（見やすいように改行をしてます。全部を見たい人はローカルに落として見てみてください。）

```python
# lambda.py
import sys

sys.setrecursionlimit(10000000)

(lambda _0: _0(input))
(lambda _1: (lambda _2: _2('Enter the flag: '))
    (lambda _3: (lambda _4: _4(_1(_3)))
        (lambda _5: (lambda _6: _6(''.join))
            (lambda _7: (lambda _8: _8(lambda _9: _7((chr(ord(c) + 12) for c in _9))))
                (lambda _10: (lambda _11: _11(''.join))
                    (lambda _12: (lambda _13: _13((chr(ord(c) - 3) for c in _10(_5))))
                        (lambda _14: (lambda _15: _15(_12(_14)))
                            (lambda _16: (lambda _17: _17(''.join))
                                (lambda _18: (lambda _19: _19(lambda _20: _18((chr(123 ^ ord(c)) for c in _20))))
                                    (lambda _21: (lambda _22: _22(''.join))
                                        (lambda _23: (lambda _24: _24((_21(c) for c in _16)))
                                            (lambda _25: (lambda _26: _26(_23(_25)))
                                                (lambda _27: (lambda _28: _28('16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'))
                                                    (lambda _29: (lambda _30: _30(''.join))
                                                        (lambda _31: (lambda _32: _32((chr(int(c,36) + 10) for c in _29.split('_'))))
                                                            (lambda _33: (lambda _34: _34(_31(_33)))
                                                                (lambda _35: (lambda _36: _36(lambda _37: lambda _38: _37 == _38))
                                                                    (lambda _39: (lambda _40: _40(print))
                                                                        (lambda _41: (lambda _42: _42(_39))
                                                                            (lambda _43: (lambda _44: _44(_27))
                                                                                (lambda _45: (lambda _46: _46(_43(_45)))
                                                                                    (lambda _47: (lambda _48: _48(_35))
                                                                                        (lambda _49: (lambda _50: _50(_47(_49)))
                                                                                            (lambda _51: (lambda _52: _52('Correct FLAG!'))
                                                                                                (lambda _53: (lambda _54: _54('Incorrect'))
                                                                                                    (lambda _55: (lambda _56: _56(_41(_53 if _51 else _55)))
                                                                                                        (lambda _57: lambda _58: _58)
                                                                                                    )
                                                                                                )
                                                                                            )
                                                                                        )
                                                                                    )
                                                                                )
                                                                            )
                                                                        )
                                                                    )
                                                                )
                                                            )
                                                        )
                                                    )
                                                )
                                            )
                                        )
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

```

この問題は、`lambda関数`というもの使って作成されているっぽいです。

lambda関数とは、無名関数とも呼ばれており、関数作成方法の一つらしい。pythonの関数作成でよく使用されるdefとは異なるものである。lambda関数は短い処理を関数化したいときに適している。lambdaは以下の要領で記述する。

    lambda 引数：処理内容

このプログラムは短いlambda関数を連続して呼び出し続けていることで、処理内容を理解しにくくしているという意図を汲み取ることができる。  
時間内にこの問題を解くためにすべてを理解して回答することは難しそうなので、chatGPTを利用してdefを用いた形式でpythonを書き直してもらうことをお願いしてみる。すると以下のような回答が返ってきた。（さすがchatGPTさま）

```python
import sys

# 再帰制限を設定
sys.setrecursionlimit(10000000)

# 入力を受け取る関数
def get_input(prompt):
    return input(prompt)

# 各文字に12を足す関数
def add_12_to_characters(s):
    return ''.join(chr(ord(c) + 12) for c in s)

# 各文字から3を引く関数
def subtract_3_from_characters(s):
    return ''.join(chr(ord(c) - 3) for c in s)

# XOR演算で各文字を変換する関数
def xor_123(s):
    return ''.join(chr(123 ^ ord(c)) for c in s)

# Base36のような文字列から元の文字に変換する関数
def decode_base36(s):
    return ''.join(chr(int(c, 36) + 10) for c in s.split('_'))

# フラグの検証を行う関数
def check_flag(user_input, correct_flag):
    return user_input == correct_flag

# フラグの検証結果を出力する関数
def print_result(is_correct):
    if is_correct:
        print("Correct FLAG!")
    else:
        print("Incorrect")

# メインの処理
def main():
    # 入力を受け取る
    user_input = get_input('Enter the flag: ')

    # 文字列の処理
    step1 = add_12_to_characters(user_input)
    step2 = subtract_3_from_characters(step1)
    step3 = xor_123(step2)
    
    # 正解のフラグを変換して得る
    correct_flag_encrypted = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'
    correct_flag = decode_base36(correct_flag_encrypted)
    
    # フラグのチェック
    is_correct = check_flag(step3, correct_flag)
    
    # 結果を出力
    print_result(is_correct)

# プログラムを実行
if __name__ == "__main__":
    main()

```

処理フローは以下のとおり
```markdown
1. 入力された文字列のUnicodeに12を足す
2. 1.で返された文字列のUicodeから3を引く
3. 2.で返された文字列のUnicodeと123のXORをとる
4. `correct_flag_encrypted`を※Base36を用いてデコードし、そのユニコードに10を足す。（※アルファベット26字と数字（0~9）10字を組み合わせてたもの。Base64の派生番と考えてもらいたい。）
5. ユーザーの入力とデコードされた文字列が等しいか比較
6. 結果表示
```
という内容である。

つまり、1.2.3.の内容を`correct_flag_encrypted`を持ちて遡るように処理をすることで結果を求めることができる。

```python
# solve.py
correct_flag_encrypted = '16_10_13_x_6t_4_1o_9_1j_7_9_1j_1o_3_6_c_1o_6r'

corect_flag = '_'.join(chr(int(c, 36) + 10) for c in correct_flag_encrypted.split('_'))

xor = lambda _xor_flag : '_'.join(chr(123 ^ ord(c)) for c in _xor_flag.split('_') )
sub_3 = lambda _sub_3_flag : '_'.join(chr(ord(c) + 3) for c in _sub_3_flag.split('_'))
sub_4 = lambda _sub_4_flag : ''.join(chr(ord(c) - 12)  for c in _sub_4_flag.split('_'))

print(sub_4(sub_3(xor(corect_flag))))

```

これを実行すると  `FLAG{l4_1a_14mbd4}`を取得することができる。