t=int(input())
for _ in range(t):
    x=int(input())
    q1=str(x)
    res=float('inf')
    for c in q1:
        res=min(res,int(c))
    print(res)