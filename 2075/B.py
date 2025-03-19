import heapq
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    heap=[]
    for i in range(n):
        heapq.heappush(heap,[-a[i],i])
    done=[0]*n
    res=0
    while(heap and k):
        ele,ind=heapq.heappop(heap)
        done[ind]=1
        res=res+(-ele)
        k-=1
    
    for i in range(n-1,-1,-1):
        if(done[i]==0):
            res+=a[i]
            break
    print(res)
