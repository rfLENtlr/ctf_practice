PixelPoker ([FlareOn9](http://flare-on.com/))

[Writeup公式](https://www.mandiant.com/sites/default/files/2022-11/02-pixelpoker.pdf)  
[他のWriteup](https://0xdf.gitlab.io/flare-on-2022/pixel_poker)

・Windows GUI アプリケーションが題材  
・GhidraはWinAPIでもいい感じにデコンパイラしてくれることが分かった．  
・が，グローバル変数の解析に失敗している．というか，静的解析ではわからないこともある．  
・x32dbgなどのWindows用動的解析ツールも併用