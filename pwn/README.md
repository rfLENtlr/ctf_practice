# ツールの使い方のメモ

## checksec
[セキュリティ機構まとめ](https://miso-24.hatenablog.com/entry/2019/10/16/021321)
## ldd
共有ライブラリへの依存関係を表示
## pwninit
glibcとリンカのバージョンを自動で揃えてくれる．特定のライブラリが配布されたときに使う．
~~~
pwninit --libc libc.so.6 --no-template --bin vuln
~~~

## objdump
### オプション
-d : ディスアセンブル


-R : 動的リロケーション情報を表示．この情報は共有ライブラリのような動的オブジェクトを使用するオブジェクトファイルに対して利用．