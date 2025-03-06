t=int(input())
for _ in range(t):
    n=int(input())
    res=[i for i in range(n)]
    for i in range(n,2):
        res[i],res[i+1]=res[i+1],res[i]
    print(res)