# Intro to RSA
[問題](https://id0-rsa.pub/problem/21/)

## 解答
- RSA暗号における法 $N$ と，暗号文 $c$ と，秘密鍵 $d$ が与えられている．
  - `N = 0x64ac4671cb4401e906cd273a2ecbc679f55b879f0ecb25eefcb377ac724ee3b1`
  - `c = 0x599f55a1b0520a19233c169b8c339f10695f9e61c92bd8fd3c17c8bba0d5677e`
  - `d = 0x431d844bdcd801460488c4d17487d9a5ccc95698301d6ab2e218e4b575d52ea3`
- 解答として期待されるフォーマットに合わせるために`sed`を使うなどして，`python3 -c "print(hex(pow(0x599f55a1b0520a19233c169b8c339f10695f9e61c92bd8fd3c17c8bba0d5677e, 0x431d844bdcd801460488c4d17487d9a5ccc95698301d6ab2e218e4b575d52ea3, 0x64ac4671cb4401e906cd273a2ecbc679f55b879f0ecb25eefcb377ac724ee3b1)))" | sed 's/^0x//`とすれば解が得られる．

