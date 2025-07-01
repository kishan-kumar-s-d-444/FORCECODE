t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    res=[]
    if(a[n-1]==0):
        q1=a.pop()
        q2=a.pop()
        for i in range(n+1):
            if(q1!=i and q2!=i):
                a.append(i)
                ans+=1
                res.append([n-1,n])
                break
    if(0 not in a):
        ans+=1
        res.append([1,len(a)])
    else:
        for i in range(1,len(a)+1):
            if(i not in a):
                ans+=1
                res.append([1,len(a)-1])
                break
        ans+=1
        res.append([1,2])
    print(ans)
    for i in range(ans):
        print(res[i][0]," ",res[i][1])