t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(b%2==0):
        q1=a*(b//2)
        if(q1%2==0):
            print(q1+2)
        else:
            print(-1)
    else:
        q1=a*b
        if(q1%2==1):
            print(q1+1)
        else:
            print(-1)
    

