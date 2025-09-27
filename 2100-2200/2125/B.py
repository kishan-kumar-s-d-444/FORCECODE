import math
t=int(input())
for _ in range(t):
    a,b,k=map(int,input().split())
    if(a==0 and b==0):
        print(0)
        continue
    if(a<=k and b<=k):
        print(1)
        continue
    if(a==b):
        print(1)
        continue
    g=math.gcd(a,b)
    na=a//g
    nb=b//g
    if(na<=k and nb<=k):
        print(1)
    else:
        print(2)
    # g=math.gcd(a,b)
    # na=a//g
    # nb=b//g
    # if(g>1):
    #     if(na<=k and nb<=k):
    #         print(1)
    #     else:
    #         reach=g*k
    #         maxi=max(na,nb)
    #         dist=maxi-reach
    #         initcost=math.ceil(dist/k)
    #         print(initcost+1)
    # else:
    #     op=1
    #     reda=math.floor(a/k)*k
    #     redb=math.floor(b/k)*k
    #     #reduced



        
        

    