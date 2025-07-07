t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=float('inf')
    cur=0
    prev=a[0]
    prevmin=a[0]
    prevmax=a[0]
    for i in range(1,n):
        if(abs(a[i-1]-a[i])<=1):
            flag=min(flag,0)
        mini=min(a[i-1],a[i])
        maxi=max(a[i-1],a[i])
        r1=prev>=mini and prev<=maxi
        r2=prev+1>=mini and prev+1<=maxi
        r3=prev-1>=mini and prev-1<=maxi
        if(r1 or r2 or r3):
            flag=min(flag,1)
    if(flag!=float('inf')):
        print(flag)
        continue
    if(flag==float('inf') and n==2):
        print(-1)
        continue
    
    

    






def fun(a):
    # q1=prevmin>=mini and prevmin<=maxi
    # q2=prevmin+1>=mini and prevmin+1<=maxi
    # q3=prevmin-1>=mini and prevmin-1<=maxi

    # p1=prevmax>=mini and prevmax<=maxi
    # p2=prevmax+1>=mini and prevmax+1<=maxi
    # p3=prevmax-1>=mini and prevmax-1<=maxi
    # if(q1 or q2 or q3 or p1 or p2 or p3):
    #     flag=cur
    # else:
    #     cur+=1
    #     prevmin=min(prevmin,a[i])
    #     prevmax=max(prevmax,a[i])
    return a
