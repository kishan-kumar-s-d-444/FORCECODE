import heapq
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    heap=[]
    for i in range(n):
        heapq.heappush(heap,[-a[i],i])
    done=[0]*n
    nk=k+1
    res=0
    while(heap and nk):
        ele,ind=heapq.heappop(heap)
        done[ind]=1
        res=res+(-ele)
        nk-=1
    print(res)
