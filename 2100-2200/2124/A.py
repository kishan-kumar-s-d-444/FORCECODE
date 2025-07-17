t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if(a==b):
        print("NO")
    else:
        print("YES")
        res=[]
        for i in range(n):
            if(a[i]!=b[i]):
                res.append(a[i])
        print(len(res))
        for i in range(len(res)):
            print(res[i],end=" ")
        print(" ")