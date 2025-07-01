t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if(sum(a)/n==float(x)):
        print("YES")
    else:
        print("NO")