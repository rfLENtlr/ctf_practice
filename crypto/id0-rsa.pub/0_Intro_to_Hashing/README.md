# Intro to Hashing
[問題](https://id0-rsa.pub/problem/18/)

## 解答
- `printf "id0-rsa.pub" | sha256sum | tr -d ' \n-' | md5sum | tr -d ' \n-'`
