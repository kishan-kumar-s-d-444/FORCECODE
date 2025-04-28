import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    low,high=min(a),max(a)
    diff=high-low
    res=math.gcd(low+diff,high+diff)
    print(res*2)