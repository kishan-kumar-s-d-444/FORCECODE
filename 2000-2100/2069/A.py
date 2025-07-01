t=int(input())
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    arr=[-1]*(n)
    num=1
    for i in range(n-2):
        if(b[i]==1):
            if(arr[i]!=-1 or arr[i+1]!=-1 or arr[i+2]!=-1):
                arr[i]=num
                arr[i+1]=num
                arr[i+2]=num
            else:
                num+=1
                arr[i]=num
                arr[i+1]=num
                arr[i+2]=num
    for i in range(n):
        if(arr[i]==-1):
            num+=1
            arr[i]=num
    print(arr)
    res="YES"
    for i in range(n-2):
        if(b[i]==0 and arr[i]==arr[i+1] and arr[i+1]==arr[i+2]):
            res="NO"
            break
        if(b[i]==1 and (arr[i]!=arr[i+1] or arr[i+1]!=arr[i+2])):
            res="NO"
            break
    print(res)
 