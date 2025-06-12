t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=1
    prev={}
    flag=True
    cur={a[0]:1}
    ind=1
    for i in range(1,n):
        if(flag):
            if(a[i] in cur):
                del cur[a[i]]
            prev[a[i]]=1
            if(not cur):
                flag=False
                ans+=1
        else:
            if(a[i] in prev):
                del prev[a[i]]
            cur[a[i]]=1
            if(not prev):
                flag=True
                ans+=1
    print(ans)

        

