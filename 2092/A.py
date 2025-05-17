import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    diff_gcd = 2
    for i in range(1, n):
        diff_gcd = math.gcd(diff_gcd, a[i] - a[i - 1])
    print(diff_gcd)