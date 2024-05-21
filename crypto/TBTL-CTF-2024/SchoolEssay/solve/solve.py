from Crypto.Util.number import inverse, long_to_bytes

def legendre_symbol(a: int, p: int) -> int:
	legendre_symbol = pow(a, (p - 1) // 2, p)
	if legendre_symbol == 1:
		return 1
	elif legendre_symbol == p - 1:
		return -1
	else:
		return 0

def mod_sqrt(a:int, p:int) -> list:
    a %= p
	
    # 1. 平方非剰余を選ぶ
    z = 2
    while legendre_symbol(z, p) != -1:
        z += 1
	
    # 2. s, Qを求める
    s = 0
    q = p - 1
    while q % 2 == 0:
        q //= 2
        s += 1
		
    # 3. M, c, t, Rの初期値を設定する
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
	
    # 4. M, c, t, Rの値を更新する
    while t != 1 :
        if t == 0: # t = 0のときは0を返す
                return [0, 0]
        i = 1
        while pow(t, pow(2, i), p) != 1:
                i += 1
        b = pow(c, pow(2, m - i - 1, p))
        m = i
        c = pow(b, 2, p)
        t = (t * b**2) % p
        r = (r * b) % p
    return [r, p - r]

N = 59557942237937483757629838075432240015613811860811898821186897952866236010569299041278104165604573
value_1 = 34994952631013563439857468985559745199379391295940238707110695903159545061311344766055629477728657
value_2 = 7906488397402721714607879953738472269409876715324979164781592447

flag2 = value_1
lower = value_2 ** 3
flag2 += N * (lower // N)

# N % 4 = 1
f1, f2 = mod_sqrt(flag2, N)

flag = long_to_bytes(f1)
print(flag)
flag = long_to_bytes(f2)
print(flag)