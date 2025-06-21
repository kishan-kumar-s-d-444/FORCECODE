from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    # for i in range(1,n):
    #     if(a[i]==a[0] and )
    mini=float('inf')
    for i in range(n):
        val=(i*a[i])+((n-i-1)*a[i])
        print(val)
        mini=min(val,mini)
    print(mini)