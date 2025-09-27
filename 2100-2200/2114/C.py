t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    prev=a[0]
    for i in range(1,n):
        if(prev+1<a[i]):
            c+=1
            prev=a[i]
    print(c)