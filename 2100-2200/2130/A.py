t=int(input())
for _ in range(t):
    n=int(input())
    S=list(map(int,input().split()))
    ans=0
    for i in range(n):
        if(S[i]==0):
            ans+=1
        else:
            ans+=S[i]
    print(ans)
