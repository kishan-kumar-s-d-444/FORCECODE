import heapq
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    heap=[]
    for i in range(n):
        heapq.heappush(heap,[-a[i],i])
    done=[0]*n
    nk=k
    res=0
    while(heap and nk):
        ele,ind=heapq.heappop(heap)
        done[ind]=1
        res=res+(-ele)
        nk-=1
    if(k==1):
        if(done[0]==1):
            res+=a[n-1]
        elif(done[n-1]==1):
            res+=a[0]
        else:
            res+=max(a[0],a[n-1])
    else:
        ele,ind=heapq.heappop(heap)
        done[ind]=1
        res=res+(-ele)
    print(res)
