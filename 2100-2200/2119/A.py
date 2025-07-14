import math
t=int(input())
for _ in range(t):
    a,b,x,y=map(int,input().split())
    if(a==b):
        print(0)
    elif(a>b):
        if(a%2==1 and a-1==b):
            print(y)
        else:
            print(-1)
    else:
        diff=b-a
        if(x<=y):
            print(diff*x)
        else:
            even=0
            for i in range(a,b):
                if(i%2==0):
                    even+=1
            odd=diff-even
            print(x*odd+y*even)

# 1 2 9021863 2413763
# 1 8 5214377 1229257