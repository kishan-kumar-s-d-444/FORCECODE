t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    flag=True
    dic2={}
    for i in range(n):
        q1=T[i]%k
        dic2[q1]=dic2.get(q1,0)+1
    for i in range(n):
        q1=S[i]%k
        key1=abs(q1-k)
        key2=q1
        if(key1 in dic2 and dic2[key1]>0):
            dic2[key1]-=1
        elif(key2 in dic2 and dic2[key2]>0):
            dic2[key2]-=1
        else:
            flag=False
            break     
    if(flag):
        print("YES")
    else:
        print("NO")
