t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=max(a)
    bits=[0]*(32)
    xor=0
    for i in range(n):
        xor+=(m^a[i])
    print(xor)
