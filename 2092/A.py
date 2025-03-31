import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    low,high=min(a),max(a)
    diff=high-low
    res=float('-inf')
    for i in range(diff+1):
        res=max(res,math.gcd(low+i,high+i))
    print(res)