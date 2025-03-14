t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    ans=0
    flag=True
    for i in range(n-1):
        if(flag and s[i]=='1'):
            ans+=1
            flag=False
        if(s[i]=='0'):
            flag=True
    print(ans)