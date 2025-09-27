def fun(a,n):
    a.sort()
    for i in range(n-1):
        if(a[i]==a[i+1]):
            return "YES"
    return "NO"
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(fun(a,n))
    