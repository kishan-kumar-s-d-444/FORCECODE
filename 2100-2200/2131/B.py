import math
t=int(input())
for _ in range(t):
    n=int(input())
    res=[-1]*(n)
    for i in range(1,n-1,2):
        res[i]=3
    if(n%2==0):
        res[n-1]=2
    for i in range(n):
        print(res[i],end=" ")
    print("\n")