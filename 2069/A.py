t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    arr=[-1]*(n)
    for i in range(n-2):
        if(b[i]==1):
            arr[i]=1
            arr[i+1]=1
            arr[i+2]=1 
    print(arr)
    res="YES"
    for i in range(n-2):
        if(b[i]==0 and arr[i]==arr[i+1] and arr[i+1]==arr[i+2]):
            res="NO"
            break
    print(res)
 