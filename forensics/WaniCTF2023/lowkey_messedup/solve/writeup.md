# My solution of lowkey_messedup
`chall.pcap` というパケットキャプチャファイルが与えれる．`WireShark` で開き，[統計] -> [プロトコル階層] を見ると，USBプロトコルが100% であることがわかる．

[このツール](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser) を使えばフラグを求めることができた．原理はわかっていないので，Future Work とする．

Usage にしたがう．
```
$ tshark -r ../chall.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > usbPcapData.txt
$ python3 usbkeyboard.py usbPcapData.txt
```

```
FLAG{Big_br0ther_is_watching_y0ur_keyb0ard}
```
