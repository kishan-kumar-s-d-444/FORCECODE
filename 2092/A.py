import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    low,high=min(a),max(a)
    diff=high-low-1-1
    res=math.gcd(low+diff,high+diff)
    print(res)