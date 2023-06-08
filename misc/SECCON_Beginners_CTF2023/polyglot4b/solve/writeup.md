# My solution of polyglot4b

## Observation
* polyglotというのは、あるファイルが、複数のプログラミング言語として実行可能であることをいうらしい。
* つまり、JPEGかつPNGかつGIFかつASCIIであるように見えるファイルを作る必要がある?
* `file -bkr sushi.jpg`の出力を見てみると`CTF4B`という文字列があるが・・・
  * `sushi.jpg` は[ここ](../given_files/sample)

## Answer1
JPEGかつPNGかつGIFかつASCIIであるように見えるファイルを作る必要があると思い込んで、そのようなファイルを作ることに腐心すると沼ってしまう。[`polyglot4b.py`](../given_files/polyglot4b.py)がどのようにpolyglotであるか判定しているかをよく見よう。

`polyglot4b.py`の47～54行目のif文の条件になっている`f_type`というのは、38～40行目のコマンドの出力結果文字列のことである。つまり、`file -bkr tmp/{f_id}/{f_id}`という **コマンドの出力結果の中に、`JPEG`、`PNG`、`GIF`、`ASCII`という文字列が含まれてさえいればよい** のである。

そこで、`file -bkr sushi.jpg`の出力結果に`CTF4B`という恣意的な文字列があったことを思い出す。後はこれを書き換えてやれば良いだけである。

```
$ cd sample
$ vi sushi.jpg  # vim上で "/CTF4B" とし、そこを"PNGGIFASCII" と書き換える

$ vi test_script.sh
# "nc localhost 31416" を"nc polyglot4b.beginners.seccon.games 31416" に書き換える

$ bash test_script.sh
ASCII/g' sushi.jpg; file sushi.jpg; cat sushi.jpg | nc polyglot4b.beginners.seccon.games 31416
sushi.jpg: JPEG image data, Exif standard: [TIFF image data, big-endian, direntries=4, description=PNGGIFASCII]
 ____       _             _       _     _____    _ _ _
|  _ \ ___ | |_   _  __ _| | ___ | |_  | ____|__| (_) |_ ___  _ __
| |_) / _ \| | | | |/ _` | |/ _ \| __| |  _| / _` | | __/ _ \| '__|
|  __/ (_) | | |_| | (_| | | (_) | |_  | |__| (_| | | || (_) | |
|_|   \___/|_|\__, |\__, |_|\___/ \__| |_____\__,_|_|\__\___/|_|
              |___/ |___/
--------------------------------------------------------------------
>> --------------------------------------------------------------------
| JPG: 🟩 | PNG: 🟩 | GIF: 🟩 | TXT: 🟩 |
FLAG: ctf4b{y0u_h4v3_fully_und3r5700d_7h15_p0ly6l07}
```

```
ctf4b{y0u_h4v3_fully_und3r5700d_7h15_p0ly6l07}
```

## Answer2
ワンライナーでカッコつける：
```
$ sed -i 's/CTF4B/PNGGIFASCII/g' sushi.jpg; cat sushi.jpg | nc polyglot4b.beginners.seccon.games 31416 | tail -n1 | awk -F ': ' '{print $2}'
ctf4b{y0u_h4v3_fully_und3r5700d_7h15_p0ly6l07}
```
