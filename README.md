# ctf_practice

## はじめに
このリポジトリは，チームで参加したCTF のWriteup や，CTF で使うツールの使い方をまとめたリポジトリです．

## 貢献のやり方
- 問題のカテゴリごとにディレクトリを作成しているので，それぞれの直下に`CTFの名前のディレクトリ`を作成してください．
- さらに問題ごとにディレクトリを作成し，直下に問題内容とWriteupへのリンクを記した `README.md` を作成してください．( `README.md` にはネタバレを載せないようにしましょう)
- 以下は，ある問題のディレクトリ構成です．このように， `Writeup` や `solver` を含むネタバレファイルは `solve` というディレクトリに置いておきましょう．

    ```
    .
    ├── README.md
    ├── assets
    │   ├── ghidra_asm.png
    │   ├── ghidra_asm2.png
    │   ├── ghidra_compare.png
    │   └── ghidra_main.png
    └── solve
        ├── solve.py
        └── writeup.md

    ```
- writeupを書く際に必要になった画像ファイルなどは， `assets` ディレクトリに置きましょう．