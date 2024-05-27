# Insanity-Check

Sanity CheckのFlag（rulesチャンネルの概要に設定されていた）とは別のFlagが[Discord](https://discord.gg/wjSVdt3a7G)上にあるので、それを探せという問題。

ひとまずDiscord上のメッセージ、スレッド、チャンネル名、チャンネルの概要等を眺めてみるも見つからない……

そこで、FlagはDiscordアプリ上では見られないと推測。

続いてWeb上で[Discord](https://discord.gg/wjSVdt3a7G)を開き、開発者ツールを使ってbotのプロフィール画像等を眺めてみるも、こちらも特に情報はなさそう。

空振りっぽかったので、今度はDiscordのAPIを利用することを考える。

DiscordのAPIを利用すると、チャンネルや役職などの情報を得ることができる。

まずは、[Discord](https://discord.gg/wjSVdt3a7G)にアクセスするためのトークンを取得する。

参考：

[Discord トークンとは何ですか? どうすれば取得できますか? - Gamingdeputy Japan](https://www.gamingdeputy.com/jp/how-tos/discord-トークンとは何ですか-どうすれば取得できます/)

[Discord の自分のアカウントの Token を取得しよう！](https://shunshun94.github.io/shared/sample/discordAccountToken)

　

Web上で[Discord](https://discord.gg/wjSVdt3a7G)を開いた状態から、開発者ツールの`ネットワーク`タブを開く。

F5キーを押してリロードし、Headers->Request Headers->authorizationの値を確認する（この値がトークン）

注意：アカウントのなりすまし等防止のため、トークンは他人に教えないようにすること！

　

続いて、トークンを使ってDiscordのAPIを動作させる。

[Discord](https://discord.gg/wjSVdt3a7G)をWebで開いた時のURLを見ると、`1233420048069296250`という番号が振られている。

これを踏まえると、以下のようなコマンドでチャンネルや役職などの情報を得ることができる（`$Token`の箇所にはトークンの値が入る）

チャンネル情報
```
curl -s -H "Authorization: $Token" https://discord.com/api/v9/guilds/1233420048069296250/channels | jq
```

役職情報
```
curl -s -H "Authorization: $Token" https://discord.com/api/v9/guilds/1233420048069296250/roles | jq
```

イベント情報
```
curl -s -H "Authorization: $Token" https://discord.com/api/v9/guilds/1233420048069296250/events | jq
```

チャンネル情報が当たりだった。

どうやら、プライベートチャンネルの名前にFlagが隠されていた模様。

```
# curl -s -H "Authorization: $Token" https://discord.com/api/v9/guilds/1233420048069296250/channels | jq | grep L3AK
    "topic": "L3AK{W3lc0ME_To_L34k_CTF!}",
    "name": "L3AK{H1dD3N_Ch4NnELs_Ar3_DR1vinG_M3_1NS4NE!}",
```

```
L3AK{H1dD3N_Ch4NnELs_Ar3_DR1vinG_M3_1NS4NE!}
```
