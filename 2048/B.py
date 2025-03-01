t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    arr=[0]*(n)
    s=k-1
    v=1
    while(s<n):
        arr[s]=v
        s=s+k
        v+=1
    for i in range(n):
        if(arr[i]==0):
            arr[i]=v
            v+=1
    for i in arr:
        print(i,end=" ")