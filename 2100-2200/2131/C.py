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
    for nm,cn in dic1.items():
        key1=abs(nm-k)
        key2=nm
        if(key1 in dic2):
            if(dic2[key1]>=cn):
                dic2[key1]=dic2[key1]-cn
                cn=0
            else:
                dic2[key1]=0
                cn-=dic2[key1]
        if(cn>0):
            if(key2 in dic2):
                dic2[key2]=dic2[key2]-cn
                cn=cn-dic2[key2]
        if(cn>0):
            flag=False
            break
    for key,val in dic2.items():
        if(val>0):
            flag=False
            break
    if(flag):
        print("YES")
    else:
        print("NO")
