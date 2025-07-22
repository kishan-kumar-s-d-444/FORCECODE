t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    maxi=max(h)
    q1=[]
    for i in range(n):
        q1.append([h[i],i])
    q1.sort()
    for i in range(n):
        if(q1[i][1]==k-1):
            k2=i
    water=0
    x=0
    flag=False
    while(1):
        if(k2==n-1):
            flag=True
            break
        cur=q1[k2][0]
        dest=q1[k2+1][0]
        time=abs(cur-dest)
        if(water+time>cur):
            break
        water+=time
        k2+=1
    if(flag):
        print("YES")
    else:
        print("NO")
