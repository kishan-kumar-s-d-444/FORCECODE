t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    while(len(arr)>1):
        a=arr.pop()
        b=arr.pop()
        arr.append(a+b-1)
    print(arr[0])
