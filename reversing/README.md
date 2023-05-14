# Reverse Engineering

## 学習の手引き
1. [CpawCTF](https://ctf.cpaw.site/)や [pico Gym](https://play.picoctf.org/practice) **(評価が80%以上のもの)** を解く

2. 過去問を解く:

    [Seccon Beginners CTF 2021](https://github.com/SECCON/Beginners_CTF_2021/tree/main/reversing)，[Wani CTF 2021](https://github.com/wani-hackase/wanictf2021-writeup/tree/main/rev)，[Anti-Debugging](https://github.com/SECCON/Beginners_CTF_2021/tree/main/reversing), [babycmp(SECCON CTF 2022)](https://github.com/SECCON/SECCON2022_online_CTF/tree/main/reversing/baby_cmp)，[Unreal Engine製ゲームのリバーシング](https://github.com/project-sekai-ctf/sekaictf-2022/tree/main/reverse/perfect-match-xtreme)，etc.

3. 復習する．その際に，いろいろな解き方を考えてみる．(複数のWriteupを漁るのがよい)


## 問題
- [Cereal Killer 01](./CerealKiller01/README.md)：Dead Face CTF 2022
- [babycmp](./babycmp/README.md)：SECCON CTF 2022  
- [Wani CTF 2023](./WaniCTF2023/README.md)
## ツールの使い方メモ
- [Ghidra](./tools/ghidra/README.md)  
- [radare2](./tools/radare2/README.md)

## 役立つリンク
### サイト
- [ELFバイナリのリバースエンジニアリング入門](https://kashiwaba-yuki.com/ctf-elf-training)：Ghida, radare2, gdbを用いてELFを解析．  
- [radare2によるバイナリ編集](https://poppycompass.hatenablog.jp/entry/2017/06/23/083824)：radare2でパッチをあてる  
- [Ghidraを使ったバイナリのパッチ方法](https://materials.rangeforce.com/tutorial/2020/04/12/Patching-Binaries/)：Ghidraのpatch instruction + Ghidra scriptでパッチをあてる  
- [List of Windows Messages](https://www.autohotkey.com/boards/viewtopic.php?t=39218)：WinAPI. WndProc関数で使われるMsgと対応する数字
### youtube
- [Self-Learning Reverse Engineering](https://www.youtube.com/watch?v=gPsYkV7-yJk&t=351s)  
- [バイナリのパッチ方法](https://www.youtube.com/watch?v=LyNyf3UM9Yc&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN&index=53)：Liveoverflow氏．Ghidra + radare2でパッチをあてる．  
- [PicoCTF2022 RE walkthrough](https://www.youtube.com/watch?v=l6Lt1sWZOUU)：Wizardlikeという問題でバイナリパッチの手法を説明．Ghidra + pwntoolsを使ったパッチ．
