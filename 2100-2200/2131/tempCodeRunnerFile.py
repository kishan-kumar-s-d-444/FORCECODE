import math
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    dic1={}
    dic2={}
    for i in range(n):
        q1=S[i]%k
        q2=abs(q1-k)
        key=min(q1,q2)
        dic1[key]=dic1.get(key,0)+1
    for i in range(n):
        q1=T[i]%k
        q2=abs(q1-k)
        key=min(q1,q2)
        dic2[key]=dic2.get(key,0)+1
        
    flag=True
    for i in range(n):
        q1=S[i]%k
        q2=abs(q1-k)
        key=min(q1,q2)
        if(dic1[key]!=dic2[key]):
            flag=False
            break    
    if(flag):
        print("YES")
    else:
        print("NO")
