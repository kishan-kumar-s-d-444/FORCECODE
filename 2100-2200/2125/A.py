t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    res=sorted(s,reverse=True)
    ans=""
    for c in res:
        ans+=c
    print(ans)
