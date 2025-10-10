t=int(input())
for _ in range(t):
    k1,k2,k3,k4=map(int,input().split())
    a,b=k1,k2
    while(max(a,b)>1 and min(a,b)>0):
        if(a>b):
            a-=2
            b-=1
        else:
            b-=2
            a-=1
    if(a>2 or b>2):
        print("NO")
        continue

    a,b=k3-k1,k4-k2
    while(max(a,b)>1 and min(a,b)>0):
        if(a>b):
            a-=2
            b-=1
        else:
            b-=2
            a-=1
    if(a>2 or b>2):
        print("NO")
        continue
    print("YES")