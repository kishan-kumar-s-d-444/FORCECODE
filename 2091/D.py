t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=(k//n)+(k%n)
    b=m
    low=1
    high=b
    while(low<=high):
        mid=(low+high)//2
        z1=b//(mid+1)
        z2=b%(mid+1)
        z3=(z1*mid)+z2
        if(z3>=a):
            high=mid-1
        else:
            low=mid+1
    print(low)