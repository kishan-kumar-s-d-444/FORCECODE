t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if(a==b):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            if(a[i]!=b[i]):
                print(1)
                print(a)
                break