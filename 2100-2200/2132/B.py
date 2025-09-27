import math
t=int(input())
for _ in range(t):
    n=int(input())
    res=[]
    for k in range(1,19):
        den=1+10**k
        if(den>n):
            break
        if(n%den==0):
            res.append(n//den)
    res.sort()
    print(len(res))
    for i in range(len(res)):
        if(i!=len(res)-1):
            print(res[i],end=" ")
        else:
            print(res[i])