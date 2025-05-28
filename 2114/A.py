import math
t=int(input())
for _ in range(t):
    s=input()
    num=int(s)
    sqnum=num**(0.5)
    sqnumi=float(math.floor(sqnum))
    if(sqnum!=sqnumi):
        print(-1)
    else:
        sqnum=int(sqnum)
        if(sqnum==0):
            a,b=0,0
        else:
            a,b=sqnum-1,1
        print(a,b)