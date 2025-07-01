t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    q=list(map(int,input().split()))
    if(n==k):
        res='1'*(m)
    elif(n-k>1):
        res='0'*(m)
    else:
        res=""
        dic={}
        for i in range(n):
            dic[i+1]=1
        for i in range(k):
            dic[q[i]]=0
        for it,vl in dic.items():
            if(vl==1):
                xor=it
                break
        for i in range(m):
            if(a[i]==xor):
                res+='1'
            else:
                res+='0'
    print(res)
