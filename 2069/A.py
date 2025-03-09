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
    num=2 
    for i in range(n):
        if(arr[i]==-1):
            arr[i]=num
            num+=1
    # print(arr)
    res="YES"
    for i in range(n-2):
        if(b[i]==0 and arr[i]==arr[i+1] and arr[i+1]==arr[i+2]):
            res="NO"
            break
        if(b[i]==1 and (arr[i]!=arr[i+1] or arr[i+1]!=arr[i+2])):
            res="NO"
            break
    print(res)
 