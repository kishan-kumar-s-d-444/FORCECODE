t=int(input())
for _ in range(t):
    k,x=map(int,input().split())
    res=[]
    a=2**k
    b=2**k
    while(1):
        if(a==x or (a<2*x and b%2==1) or (a>=2*x and a%2==1)):
            break
        elif(a<2*x):
            res.append(2)
            a+=(b//2)
            b=b//2
        elif(a>=2*x):
            res.append(1)
            b+=(a//2)
            a=a//2
    if(a!=x):
        res=[]
        a,b=2**k,2**k
        x=2**(k+1)-x
        while(1):
            if(b==x):
                break
            elif(b<2*x):
                res.append(1)
                b+=(a//2)
                a=a//2
            elif(b>=2*x):
                res.append(2)
                a+=(b//2)
                b=b//2
    print(len(res))
    for i in range(len(res)):
        if(i!=len(res)-1):
            print(res[i],end=" ")
        else:
            print(res[i])
            print("\n")
    
    