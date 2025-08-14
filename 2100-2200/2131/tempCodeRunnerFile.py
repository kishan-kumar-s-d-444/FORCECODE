t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    S=list(map(int,input().split()))
    T=list(map(int,input().split()))
    dic1={}
    dic2={}
    for i in range(n):
        q1=S[i]//k
        q2=S[i]-(q1*k)
        dic1[q2]=dic1.get(q2,0)+1
        r1=T[i]//k
        r2=T[i]-(r1*k)
        dic2[r2]=dic2.get(r2,0)+1
    flag=True
    for nm,cn in dic1.items():
        key=abs(nm-k)
        if(key in dic2 and dic2[key]==cn):
            continue
        else:
            flag=False
            break
    if(flag):
        print("YES")
    else:
        print("NO")
