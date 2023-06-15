# My solution of Three
`three` というバイナリが与えられている．
ひとまず`strings`コマンドを試してみるが，FLAGは見つからない．
という訳で，Ghidraさんに頼る．

main関数の内容をDecompilerで眺めると，`validate_flag`といういかにも怪しげな関数が見つかる．

