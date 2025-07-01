t=int(input())
for _ in range(t):
    n=int(input())
    s=str(n)
    m=len(s)
    z=0
    res=float('inf')
    for i in range(m):
        if(s[i]=='0'):
            z+=1
        else:
            r=m-i-1
            l=i-z
            res=min(res,l+r)
    print(res)

