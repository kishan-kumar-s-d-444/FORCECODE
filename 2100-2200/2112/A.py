t=int(input())
for _ in range(t):
    a,x,y=map(int,input().split())
    atox=abs(a-x)
    atoy=abs(a-y)
    flag=False
    for point in range(min(x,y),max(x,y)+1):
        btox=abs(point-x)
        btoy=abs(point-y)
        if(btox<atox and btoy<atoy):
            flag=True
            break
    if(flag):
        print("YES")
    else:
        print("NO")

        
       