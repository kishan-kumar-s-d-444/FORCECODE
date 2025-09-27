t=int(input())
for _ in range(t):
    n,k,x=map(int,input().split())
    a=list(map(int,input().split()))
    s=sum(a)
    l=0
    r=(k*n)-1
    if(s*k<x):
        print(0)
    else:
        q1=x//s
        q2=x%s
        if(q1>0 and q2!=0):
            r=r-(q1*n)
        elif(q1>0 and q2==0):
            r=r-(q1*n)
            r+=1
        q3=0
        for i in range(n-1,-1,-1):
            q3+=a[i]
            if(q3>=q2):
                break
            else:
                r-=1
        # print(l,r)
        print(max(0,r-l+1))

