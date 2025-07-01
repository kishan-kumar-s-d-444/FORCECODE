import math
t=int(input())
for _ in range(t):
    n,k,p=map(int,input().split())
    if(n*p<k):
        print(-1)
    elif(n*(-p)>k):
        print(-1)
    else:
        if(k==0):
            print(0)
        elif(k>0):
            ans=math.ceil(k/p)
            print(ans)
        else:
            k=-k
            ans=math.ceil(k/p)
            print(ans)