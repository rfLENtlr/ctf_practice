# My solution for do_not_rewrite

## 方針

まずは，実行ファイルのセキュリティ機構を確認．
- RELRO: Full RELRO
- STACK CANARY: Canary found
- NX: NX enabled
- PIE: PIE enabled

配布された`main.c`を読むと，`show_flag()`を呼び出せばFLAGが手に入ることが分かる．  
ASLRが有効なため，`show_flag()`のアドレスは実行する度に変化するが，ヒントとして初めに教えてくれる．

また，`main()`で構造体の配列`ingredients[3]`が定義されているが，その後のfor文で`i=3`の時に配列外を書き換えてしまうバグがあることが分かる．

すなわち，`i=3`の時の標準入力を利用して，`main()`のリターンアドレスを`show_flag()`のアドレスに書き換えればよい．  
ただしSSPが有効なため，Canaryを書き換えないように注意する必要がある．

## 解法

はじめに，`main()`のリターンアドレスが格納されているスタックのアドレスをgdbで調べる．  
次に，`i=3`の時の標準入力の内容が格納されるスタックのアドレスを調べる．  
その結果，`main()`のリターンアドレスが格納されているアドレスに，`i=3`の`name`が格納されることが分かる．  
よって，`i=3`の`name`として`show_flag()`のアドレスを入力すれば良い．  
※ 正確にはアドレスに8を加えたもの（スタックのアライメント）

`calories_per_gram`と`amount_in_grams`はCanaryの場所に相当するが，`+`を入力することで書き換えを回避できる．

詳細は [solve.py](./solve.py) を参照．

## 参考リンク

- [Pwnにおけるスタックのアライメント](https://sok1.hatenablog.com/entry/2022/01/17/050710)