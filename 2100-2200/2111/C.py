from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    mini=float('inf')
    for i in range(n):
        val=(i*a[i])+((n-i-1)*a[i])
        print(val)
        mini=min(val,mini)
    print(mini)