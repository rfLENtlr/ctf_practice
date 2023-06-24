# My solution for web_assembly
https://wasm-rev.wanictf.org/ にアクセスすると，ユーザ名とパスワードの入力を求められる．もちろん分からない．開発者ツールのソースを開くと `index.wasm` を見つけることができる．しかし，開発者ツールで見えているのは `WAT`というWASM のテキスト表現のようだ．WASMが欲しいので，Chat GPT に聞いてみた．

```
Webブラウザの開発者ツールでwasmファイルを見つけた場合、そのファイルを直接ダウンロードすることはできません。ただし、次の手順に従って、開発者ツールを使用してwasmファイルを取得することができます。

1. 開発者ツールを開きます（Ctrl + Shift + IまたはCmd + Option + Iを押します）。
2. ページでwasmファイルを探します。Webページを読み込むと、ブラウザのネットワークタブにリクエストが表示されます。wasmファイルは、.wasm拡張子を持つファイルです。
3. wasmファイルのリクエストを選択し、右クリックして、「リンクアドレスをコピー」を選択します。
4. 新しいタブを開き、アドレスバーにコピーしたリンクアドレスを貼り付けて、Enterキーを押します。
5. ブラウザは、wasmファイルをダウンロードし、保存するかどうかを確認するダイアログボックスを表示します。必要に応じて、保存する場所を指定して保存してください。

以上の手順で、Webブラウザの開発者ツールを使用してwasmファイルをダウンロードできます。ただし、wasmファイルがプライベートなものである場合は、そのファイルをダウンロードする前に、適切な権限を取得する必要がある場合があります。
```

教えてもらったとおりのことを行い，`index.wasm` をダウンロードした．
[wabt](https://github.com/WebAssembly/wabt) というツールキットに含まれる`wasm-decompile` を使い，decompileしてみた．
```
$ wasm-decompile index.wasm -o index.dcmp 
```

`index.dcmp` を眺めると，怪しいところがある．
`3r!}` はいかにもフラグの一部だろう．しかし，FridayやJunなどのいらないものが混じっていて読みにくい．
```
data d_3rinfinityFebruaryJanuaryJul(offset: 65536) =
  "3r!}\00infinity\00February\00January\00July\00Thursday\00Tuesday\00Wed"
  "nesday\00Saturday\00Sunday\00Monday\00Friday\00May\00%m/%d/%y\004n_3x\00"
  "-+   0X0x\00-0X+0X 0X-0x+0x 0x\00Nov\00Thu\00unsupported locale for st"
  "andard input\00August\00Oct\00Sat\000us\00Apr\00vector\00October\00Nov"
  "ember\00September\00December\00ios_base::clear\00Mar\00p_0n_Br\00Sep\00"
  "3cut3_Cp\00%I:%M:%S %p\00Sun\00Jun\00Mon\00nan\00Jan\00Jul\00ll\00Apri"
  "l\00Fri\00March\00Aug\00basic_string\00inf\00%.0Lf\00%Lf\00true\00Tue\00"
  "false\00June\00Wed\00Dec\00Feb\00Fla\00ckwajea\00%a %b %d %H:%M:%S %Y\00"
  "POSIX\00%H:%M:%S\00NAN\00PM\00AM\00LC_ALL\00LANG\00INF\00g{Y0u_C\00012"
  "3456789\00C.UTF-8\00.\00(null)\00Incorrect!\00Pure virtual function ca"
  "lled!\00Correct!! Flag is here!!\00feag5gwea1411_efae!!\00libc++abi: \00"
  "Your UserName : \00Your PassWord : \00\00\00\00\00\00L\04\01\00\02\00\00"
  "\00\03\00\00\00\04\00\00\00\05\00\00\00\06\00\00\00\07\00\00\00\08\00\00"
  "\00\09\00\00\00\0a\00\00\00\0b\00\00\00\0c\00\00\00\0d\00\00\00\0e\00\00"
  "\00\0f\00\00\00\08\00\00\00\00\00\00\00\84\04\01\00\10\00\00\00\11\00\00"
```

`\00` と `\`を空白で置換してやると少し見やすくなった．
```
"3r!}  infinity  February  January  July  Thursday  Tuesday  Wed"
  "nesday  Saturday  Sunday  Monday  Friday  May  %m/%d/%y  4n_3x  "
  "-+   0X0x  -0X+0X 0X-0x+0x 0x  Nov  Thu  unsupported locale for st"
  "andard input  August  Oct  Sat  0us  Apr  vector  October  Nov"
  "ember  September  December  ios_base::clear  Mar  p_0n_Br  Sep  "
  "3cut3_Cp  %I:%M:%S %p  Sun  Jun  Mon  nan  Jan  Jul  ll  Apri"
  "l  Fri  March  Aug  basic_string  inf  %.0Lf  %Lf  true  Tue  "
  "false  June  Wed  Dec  Feb  Fla  ckwajea  %a %b %d %H:%M:%S %Y  "
  "POSIX  %H:%M:%S  NAN  PM  AM  LC_ALL  LANG  INF  g{Y0u_C  012"
  "3456789  C.UTF-8  .  (null)  Incorrect!  Pure virtual function ca"
  "lled!  Correct!! Flag is here!!  feag5gwea1411_efae!!  libc++abi:   "
  "Your UserName :   Your PassWord :             L 04 01   02    "
  "   03       04       05       06       07       08    "
  "   09       0a       0b       0c       0d       0e    "
  "   0f       08               84 04 01   10       11    "
```

明らか必要でないものを手作業で消す．
```
"3r!}  4n_3x  0us  p_0n_Br  3cut3_Cp  ckwajea  {Y0u_C  feag5gwea1411_efae!!
```
リートで意味がつながるように構成しなおすと，
`{Y0u_C4n_3x3cut3_Cpp_0n_Br0us3r!}` が求まる．ちなみに，ユーザ名とパスワードも含まれており，ユーザ名は`ckwajea`，パスワードは`feag5gwea1411_efae!!` であった．