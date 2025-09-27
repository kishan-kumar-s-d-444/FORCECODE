import math
t=int(input())
for _ in range(t):
    n=int(input())
    ran=math.ceil(math.log(n,3))
    # print("range",ran)
    cost=0
    while(1):
        if(n==0):
            break
        if(n>=3**ran):
            n=n-3**ran
            cost+=(3**(ran+1))
            cost+=((3**(ran-1))*ran)
        else:
            ran-=1
    print(int(cost))


#243  1134