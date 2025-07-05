t=int(input())
for _ in range(t):
    a,x,y=map(int,input().split())
    d1=abs(a-x)
    d2=abs(x-y)
    d3=abs(a-y)
    if(d1>=d2 and d3>=d2):
        print("YES")
    else:
        print("NO")
        
        