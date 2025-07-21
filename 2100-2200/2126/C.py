from re import L


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
            k1=q1[i][0]
            k2=i
    water=1
    x=0
    flag=False
    cur=k1
    while(1):
        if(k2==n-1):
            flag=True
            break
        if(cur<water):
            break
        mom=x+abs(k1-q1[k2+1][0])
        water+=1
        x=mom
        cur=q1[k2+1][0]
        k2+=1
        
    if(flag):
        print("YES")
    else:
        print("NO")
