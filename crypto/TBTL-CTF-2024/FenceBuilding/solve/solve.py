s="T0n40g5BG03cmk0D1hr}T{dFe_3g_3buL_5_n0"

L=len(s)
for i in range(2,len(s)):
    ans = ["."] * len(s)
    p=0
    x=(i-1)*2
    down=True
    for j in range(i):
        k=j
        a=True
        while k<len(s) and p<len(s):
            ans[k]=s[p]
            p+=1
            if x!=(i-1)*2:
                if a:
                    k+=x
                    a=False
                else:
                    k+=(i-1)*2-x
                    a=True
            else:
                k+=x
        if down:
            x-=2
            if x==0:
                x=(i-1)*2
    for i in range(len(s)):
        print(ans[i],end="")
    print(" ")