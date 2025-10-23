t=int(input())
for _ in range(t):
    x=int(input())
    cur=0
    take=x
    while(take):
        cur+=(take%10)
        take=take//10
    need=9-cur%9
    k=0
    while(1):
        y=9*k+need
        xy=int(str(x)+str(y))
        div=x+y
        if(xy%div==0):
            print(y)
            break
        k+=1

    