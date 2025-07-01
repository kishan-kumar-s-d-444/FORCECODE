t=int(input())
for _ in range(t):
    n=int(input())
    if(n%2==0):
        print(-1)
    else:
        for i in range(n+1):
            print(i+1,end=" ")