# babycmp (SECCON CTF 2022)

## 静的解析
実行してみると，コマンドライン引数でFlagを入力しないといけないことがわかる．求めたいものを入力することは不可能なので，いつものようにリバースエンジニアリングを行い比較処理を解読する必要がある．
<figure><img src="../assets/usage.png" alt=""><img src="../assets/main2.png" alt=""><figcaption></figcaption></figure>

シンボル情報が消されているわけでもないので，Ghidraで静的解析を行うとmain関数がすぐに見つかる．
Ghidraのデコンパイル結果の変数が分かりにくいので，[Rename Variable]や[Retype Variable]で変数名や型を変更しておく．
<figure><img src="../assets/decompiler2.png" alt=""><img src="../assets/main2.png" alt=""><figcaption></figcaption></figure>
<figure><img src="../assets/decompile.png" alt=""><img src="../assets/main2.png" alt=""><figcaption>main関数のデコンパイル結果</figcaption></figure>

main関数で行っている処理は大きく分けて二つで，
1. コマンドライン引数で入力した文字列(argv[1])のそれぞれの文字を何かとXORしている．(60行～67行)
2. 1でXORを取った文字列が内部のバイト列と一致していたらCorrect!を出力．(71行～78行)
である．

XORなので，逆の処理を書けば良い．
    ちなみに，デコンパイル結果にあるSUB168やZEXT816はGhidra独自の組み込み関数のようなもの．うまくPコードからデコンパイルできなかったときに表示されるらしい．
    リファレンスは，[Help] > [Contents]で開くGhidra Helpで検索すれば，Ghidra Conceptsというページに詳しく書かれている． 

    例えば，ZEXT14は1バイトを4バイトにゼロ拡張する．

    ZEXT14(x) - Zero-extension operator - INT_ZEXT
        ・The digit '1' indicates the size of the input operand 'x' in bytes.
        ・The digit '4' indicates the size of the output in bytes.
            ZEXT24(0xaabb) = 0x0000aabb



## 復号スクリプト
CONCAT44は4バイトと4バイトを連結する関数のようなもので，71行目から比較しているバイト列は
```math 
uStack_44 + local_48 + uStack_3c + uStack_40 + uStack_34 + local_38 + uStack_2c + uStack_30 + local_28
```
なので，
```python
b'\x59\x1e\x23\x20\x20\x2f\x20\x04\x2b\x2d\x36\x75\x35\x7f\x1a\x44\x07\x36\x50\x6d\x03\x5a\x17\x11\x36\x2b\x47\x04\x01\x09\x3c\x15\x38\x0a\x41'
```
と考えた．このバイト列からflagは35文字であることが分かる．