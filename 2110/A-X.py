from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=Counter(a)
    a.sort()
    if((a[0]+a[-1])%2==0):
        print(0)
    else:
        print(max(count[a[0]],count[a[-1]]))
