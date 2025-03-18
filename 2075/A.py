import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    ans=0
    if(n%2==1):
        if(k%2==1):
            n=n-k
        else:
            n=n-k-1
        ans=1
    
    if(k%2==1):
        k=k-1
    ans=ans+math.ceil(n/k)
    print(ans)
    