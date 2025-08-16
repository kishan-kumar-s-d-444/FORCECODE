t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    dic1={}
    dic2={}
    for i in range(n):
        q1=S[i]%k
        dic1[q1]=dic1.get(q1,0)+1
    for i in range(n):
        q1=T[i]%k
        dic2[q1]=dic2.get(q1,0)+1
        
    flag=True
    if(dic1.get(0,0)!=dic2.get(0,0)):
        flag=False
    if(k%2==0 and dic1.get(k//2,0)!=dic2.get(k//2,0)):
        flag=False
    limit=k//2
    r=1
    while(flag and r<=limit):
        it1=dic1.get(r,0)+dic1.get(abs(k-r),0)
        it2=dic2.get(r,0)+dic2.get(abs(k-r),0)
        if(it1!=it2):
            flag=False
        r+=1
    if(flag):
        print("YES")
    else:
        print("NO")
