t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    res=[0]*(n)
    ind=1
    for i in range(n):
        if(s[i]=='1'):
            res[i]=ind
            ind+=1
    for i in range(n):
        if(s[i]=='0'):
            res[i]=ind
            ind+=1
    maxi=0
    one=0
    for i in range(n):
        if(s[i]=='1'):
            one+=1
        else:
            one=0
        maxi=max(maxi,one)
    
    if(maxi>=k):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            if(i==n-1):
                print(res[i])
            else:
                print(res[i],end=" ")
        

