t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    cards=[]
    dic={}
    for i in range(n):
        arr=list(map(int,input().split()))
        arr.sort()
        for it in arr:
            dic[it]=i+1
        cards.append(arr)
    res=[]
    flag=True
    ind=0
    for i in range(n*m):
        if(len(res)<n):
            res.append(dic[i])
            if(i+1<n*m-1 and dic[i+1]==dic[i]):
                flag=False
                break
        else:
            if(dic[i]!=res[ind]):
                flag=False
                break
            ind=(ind+1)%n
    if(flag):
        for a in res:
            print(a,end=" ")
    else:
        print(-1)