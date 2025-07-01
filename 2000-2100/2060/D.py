t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=True
    for i in range(n-1):
        mini=min(a[i],a[i+1])
        a[i]=a[i]-mini
        a[i+1]=a[i+1]-mini
        if(a[i]>a[i+1]):
            flag=False
            break
    if(flag):
        print("Yes")
    else:
        print("No")