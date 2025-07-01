t=int(input())
for _ in range(t):
    x,y,a=map(int,input().split())
    a=a+0.5
    v=a//(x+y)
    cur=(x+y)*(v)
    if(cur+x>=a):
        print("No")
    else:
        print("Yes")

