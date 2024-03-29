# My solution for Did_it!

## 概要
* [did.py](../given_files/did.py) の 42 行目が脆弱性になっている
* 大まかに以下の流れでフラグを得る：
  * クエリを工夫すれば、ある整数 $n$ が集合 $K$ に含まれるか否かは2回のクエリで判定できることが分かる。
  * 1 回のクエリで最大 20 個の整数を入力できるので、 2 回のクエリで 20 個の整数に対しそれらが $K$ の元か判定できる。
  * ということは、 12 回のクエリで 120 個の整数に対しそれらが $K$ の元かを判定できる。
  *  $K$ の全ての元は 0 以上 126 以下の整数なので、ソルバを数回実行すればフラグが得られる。
* ソルバー：[solve.py](./solve.py)

## 解答
### 1. [did.py](../given_files/did.py) を理解する
まず、 43 行目の条件 `set(_A) == set(K)` が真になれば、フラグが出力されることが分かる。
ここで `_A` はユーザの入力により作られる整数の集合で、 `K` はサーバでランダムに作られる整数の集合である。また、それぞれの集合の要素数は最大 20 個であり、全ての元は 0 以上 126 以下の整数である。つまり、 `K` を当てれば勝ちということである。

さて、 `K` を当てるための情報として与えられているのが、 42 行目の `DID` の出力である。 
`DID` は、 ユーザの入力である `_A` と当てたい `K` との差集合の各元 $n$ に対して、 $n^2\ \text{mod}\ 127 + \textsf{randint(0か1)}$ を計算し **(集合ではなく) リストとして** 出力してくれる。

サーバーへのクエリの入力回数は 51 行目で制御されており、 13 回と制限が設けられている。

### 2. `DID` を用いて、ある整数 $n$ が $K$ の元かを特定する方法を考える
前述の通り、 `DID` は `_A` と `K` の差集合の各元 $n$ に対し、 $n^2\ \text{mod}\ 127 + \textsf{randint}(0,1)$ を計算し **(集合ではなく) リストとして** 出力する。さて、 `DID` の出力からどのように `K` を特定するかを以下で述べる。

具体例として、 $\bar{A} = \{3, 124\}, K = \{124, 10, 2\}$ のときを考える。
この時、 $\bar{A} - K = \{3\}$ なので、 $\textsf{DID} = [9]$ となる。( $+ \textsf{randint}(0,1)$ は本質でないので一旦無視する。)

さて、こうすると少し困ったことが起こる。我々は $\textsf{DID}$ から $K$ を当てなければならないのだが、 $[9]$ という出力だけからそれを判定することはできない。
なぜなら、 $n^2\ \text{mod}\ 127 == 9$ となる $n$ は 3 と 124 の2種があるからだ。そして一般に、 $n^2\ \text{mod}\ 127 == r^2$ となる $n$ は $r, 127 - r$ の2種となる。

これを解決するには、 $\bar{A} = \{3, 124\}$ を送ったのち $\bar{A} = \{3\}$ を送ればよい。もしこの2回目の応答として $\textsf{DID} = []$ が返ってきた場合、 3 が $K$ に含まれていたことが判明し、 $\textsf{DID} = [9]$ が返ってきた場合、 124 が $K$ に含まれていたことが判明する。

この例では $\bar{A} = \{3, (127 - 3)\}$ を送っていたが、1 クエリ内に格納できる整数は 20 個までなので、 $\{n_1, (127 - n_1), ... , n_{10}, (127 - n_{10})\}$ を1回のクエリとして送信すると効率的である。 そして $\textsf{DID}$ の出力に応じて 2 度目のクエリ ( $\bar{A} = \{n_1, n_4, n_11\}$ のようになる) を送る。これを 6 回 (つまり 12 クエリ分) 繰り返せば、 120 個の整数に対しそれが $K$ の元であるかを判定することができる。

### 3. `+ randint(0,1)` に対処する
結論としては、 $n_1^2\ \text{mod}\ 127$ と $n_2^2\ \text{mod}\ 127$ の値の差が 1 以下の数 (例えば 1 と 111 など) を同じクエリ内に入れないようにすればよい。

### 4. ソルバを実装する
まず、 3. の条件を満たすようなクエリを作成する。
```python
# tool.py
# 二乗して127で割った余りを昇順でソート
l = sorted([(pow(i,2,127), i) for i in range(127)])

# 隣り合う数の pow(i,2,127) の差が 2 以上になるよう工夫
for i in range(1,32):
    print(f"{l[4*i-1][1]},{l[4*i][1]},", end='')
for i in range(1,33):
    print(f"{l[4*i-3][1]},{l[4*i-2][1]},", end='')
```

```console
$ python3 tool.py
16,111,32,95,30,97,53,74,12,115,20,107,28,99,36,91,44,83,62,65,6,121,61,66,13,114,38,89,47,80,21,106,58,69,24,103,18,109,31,96,57,70,29,98,35,92,50,77,27,100,37,90,22,105,19,108,49,78,45,82,54,73,1,126,2,125,3,124,34,93,4,123,48,79,23,104,5,122,41,86,63,64,17,110,52,75,26,101,60,67,7,120,59,68,51,76,8,119,14,113,43,84,33,94,40,87,9,118,46,81,56,71,15,112,10,117,55,72,42,85,25,102,11,116,39,88
```

これをエディタでちまちまいじり、以下のようにクエリのリストを作成する
```python
q = [
    b"16, 111, 32, 95, 30, 97, 53, 74, 12, 115, 20, 107, 28, 99, 36, 91, 44, 83, 62, 65",
    b"6, 121, 61, 66, 13, 114, 38, 89, 47, 80, 21, 106, 58, 69, 24, 103, 18, 109, 31, 96",
    b"57, 70, 29, 98, 35, 92, 50, 77, 27, 100, 37, 90, 22, 105, 19, 108, 49, 78, 45, 82",
    b"54, 73, 1, 126, 2, 125, 3, 124, 34, 93, 4, 123, 48, 79, 23, 104, 5, 122, 41, 86",
    b"63, 64, 17, 110, 52, 75, 26, 101, 60, 67, 7, 120, 59, 68, 51, 76, 8, 119, 14, 113",
    b"43, 84, 33, 94, 40, 87, 9, 118, 46, 81, 56, 71, 15, 112, 10, 117, 55, 72, 42, 85",
    b"25, 102, 11, 116, 39, 88, 0",
]
```


次に、 2. の内容を実装すると以下のようになる：
```python
r = remote('01.cr.yp.toc.tf', 11337)
r.recvline()
r.recvline()
r.recvline()

# K
in_K = []

for i in range(6):
    # ----- クエリ1回目 ----- #
    r.sendline(q[i])
    r.recvuntil(b'DID = ')
    # ----- クエリ1回目 ----- #

    # 受け取ったデータを python のリストとして格納
    rcv = r.recvline().strip().decode()
    res_nums = list(map(int, rcv.strip('[]').split(','))) if rcv != '[]' else []

    # 送信したデータを整数リスト化
    req_nums = list(map(int, q[i].decode().strip('[]').split(',')))

    # 受け取ったデータに対し、req_nums[2*i]^2 mod 127, .. + 1 を満たす要素の個数
    # req_nums[2*i]の2乗か2乗+1 が含まれているなら保留して次のクエリとする。
    next_req_nums = []
    for i in range(len(req_nums)//2):
        if len(list(filter(lambda res: res == pow(req_nums[2*i],2,127) or res == pow(req_nums[2*i],2,127)+1, res_nums))) <= 1:
            next_req_nums.append(req_nums[2*i])
    if next_req_nums == []: continue

    # ----- クエリ2回目 ----- #
    r.sendline(str(next_req_nums).strip('[]').encode()+b','+q[6])
    r.recvuntil(b'DID = ')
    # ----- クエリ2回目 ----- #

    # 受け取ったデータを python のリストとして格納
    rcv = r.recvline().strip().decode()
    res_nums = list(map(int, rcv.strip('[]').split(','))) if rcv != '[]' else []

    # K の元を特定する：
    # 2回目のクエリ時にA-K に含まれているなら、Kにはその相方が含まれていたことになる
    for next_req_num in next_req_nums:
        if pow(next_req_num,2,127) in res_nums or pow(next_req_num,2,127) + 1 in res_nums:
            in_K.append(127 - next_req_num)
        else:
            in_K.append(next_req_num)

r.sendline(','.join(map(str, list(in_K))).encode())
r.recvline().decode()
stri = r.recvline().decode()
print(stri)
r.close()
```

あとは `stri` に `CCTF` が含まれるまで while ループを回せばよい
```console
$ python3 solve.py
...
+ Congrats! the flag: CCTF{W4rM_Up_CrYpt0_Ch4Ll3n9e!!}
```
