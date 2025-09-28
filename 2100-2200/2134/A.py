t=int(input())
for _ in range(t):
    n,a,b=map(int,input().split())
    if((n%2)^(b%2)==1):
        print("No")
    elif((n%2)^(a%2)==1 and a>b):
        print("No")
    else:
        print("Yes")

