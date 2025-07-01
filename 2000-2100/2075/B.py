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
    if(k==1):
        while(heap):
            ele,ind=heapq.heappop(heap)
            if(ind!=0 and ind!=n-1):
                res+=a[ind]
                break
        res+=max(a[0],a[n-1])
    else:
        temp=[]
        prev=0
        while(heap and k):
            ele,ind=heapq.heappop(heap)
            done[ind]=1
            temp.append([prev,ind])
            prev=ind
            res+=a[ind]
            k-=1
        temp.append([prev,n])
        maxi=float('-inf')
        # print(temp,"k")
        for l,r in temp:
            if(r-l>1):
                # print(a[l+1:r],"i")
                maxi=max(maxi,max(a[l+1:r]))
        res+=maxi
    print(res)
