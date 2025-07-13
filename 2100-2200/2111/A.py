import math
t=int(input())
for _ in range(t):
    x=int(input())
    if(x==1):
        print(3)
        continue
    q1=math.floor(math.log(x,2))
    print(q1*2+3)
