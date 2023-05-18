# My solution of beg_for_a_peg
`log.pcapng` が与えられる．Wiresharkで開き，`[プロトコル階層]` を調べると，JPEG File Interchange Format がある．WireShark の `[ファイル] -> [オブジェクトをエクスポート] -> [http]` を選択し，JPEGを抽出してみる．

すると，`flag.jpg` の断片のようなファイルが複数抽出されている．（断片なので，単体では開くことができない．）

そこで，それぞれのファイルを合成しようと思ったがめんどくさそうだったので，生のバイナリから抽出することにした．

No.31に `GET /flag.jpg HTTP/1.1` とあるので，
右クリックし，`[追跡] -> [TCP ストリーム] ` を開き，`198.51.100.1:4500 -> 192.168.0.16:63559` のデータを `Raw形式` で保存する．

保存したバイナリから JPEG を抽出するには，`binwalk` を用いる．
```bash
$ binwalk raw.bin
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
68            0x44            JPEG image data, EXIF standard
80            0x50            TIFF image data, big-endian, offset of first image directory: 8
```
上手く抽出できなかったが，[この記事](https://qiita.com/out_of_stack/items/1e85eded0a7f115b369a)を参考に拡張子を指定すると抽出できた．

```
binwalk --dd=".*" raw.bin 
```
<figure><img src="../assets/44" alt=""></figure>

