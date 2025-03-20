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
    if(done[0]==0 and done[n-1]==0):
        res+=max(a[0],a[n-1])
    elif(done[0]==0):
        i=n-1
        maxi=float('-inf')
        while(i>=0):
            rv=float('-inf')
            while(i>=0 and done[i]==0):
                rv=max(rv,a[i])
                i-=1
            if(i<0):
                rv=a[0]
            else:
                i-=1
            max=max(maxi,rv)
        res+=maxi
    elif(done[n-1]==0):
        i=0
        maxi=float('-inf')
        while(i<n):
            rv=float('-inf')
            while(i<n and done[i]==0):
                rv=max(rv,a[i])
                i+=1
            if(i==n):
                rv=a[0]
            else:
                i-=1
            max=max(maxi,rv)
        res+=maxi
    else:
        maxi=float('-inf')
        for i in range(n):
            if(done[i]==0):
                maxi=max(maxi,a[i])
        res+=maxi
    print(res)
