t=int(input())
for _ in range(t):
    n=int(input())
    if(n%2==0):
        print(-1)
    else:
        res=[0]*(n)
        for i in range(n):
            res[i]=((i+i)%n)+1
        for i in range(n):
            print(res[i],end=" ")
    print("\n")