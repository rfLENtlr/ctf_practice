# My solution for Aztecs

配布ファイルとして[png画像](../given_files/challenge.png)が1枚与えられる。

<img src="../given_files/challenge.png" width="30%">

どうやらAztec codeと呼ばれるコードの模様（タイトル回収）

参考：[Aztec コードにおけるシンボル | Cognex](https://www.cognex.com/ja-jp/resources/symbologies/2-d-matrix-codes/aztec-codes)

本来、Aztec codeはモノクロ画像のはずだが、RGBで表現されたカラフルな画像になっている

→RGBで描かれたAztec Codeが三枚重なっていると予想

PythonでRGBの要素を抜き出してAztec codeを生成するプログラムを作成する。

[作成したプログラム](./solve.c)を動かし、RGBそれぞれのAztec codeを生成する（生成結果は以下の通り）

<img src="../assets/redshare.png" width="30%">
<img src="../assets/blueshare.png" width="30%">
<img src="../assets/greenshare.png" width="30%">

それぞれのAztec codeを読み取ると、以下のような文字列が出てくる

```
L3AK{d0_YOu_r34L1y_T
```
```
hINk_7H3_aNCi3n7_4z7
```
```
Ec5_kn3W_B4rc0De5}
```

つなげてFlagを獲得

```
L3AK{d0_YOu_r34L1y_ThINk_7H3_aNCi3n7_4z7Ec5_kn3W_B4rc0De5}
```
