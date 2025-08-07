t=int(input())
for _ in range(t):
    n,s=map(int,input().split())
    a=list(map(int,input().split()))
    if(sum(a)%n==0):
        print(-1)
    else:
        print([i+1 for i in range(n)])
    
