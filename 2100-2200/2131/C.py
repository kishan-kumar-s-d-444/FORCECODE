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
    # print(dic1)
    # print(dic2)

    flag=True
    for nm,cnt in dic1.items():
        key1=abs(nm-k)
        key2=nm
        if(key1 in dic2):
            if(dic2[key1]>=dic1[nm]):
                dic2[key1]=dic2[key1]-dic1[nm]
                dic1[nm]=0
            else:
                dic1[nm]=dic1[nm]-dic2[key1]
                dic2[key1]=0
        if(dic1[nm]>0):
            if(key2 in dic2 and dic2[key2]>=dic1[nm]):
                dic2[key2]=dic2[key2]-dic1[nm]
                dic1[nm]=0
            else:
                flag=False
                break
        if(dic1[nm]>0):
            flag=False
            break
        # print("HI",dic1,dic2)
    for v in dic2.values():
        if(v>0):
            flag=False
            break
    for v in dic1.values():
        if(v>0):
            flag=False
            break
    if(flag):
        print("YES")
    else:
        print("NO")
