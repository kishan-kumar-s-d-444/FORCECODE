t=int(input())
for _ in range(t):
    n,m,l,r=map(int,input().split())
    inter=n-m
    flag=True
    while(inter):
        if(flag):
            r-=1
            if(l<0):
                flag=False
        else:
            l+=1
            if(r>0):
                flag=True
        inter-=1
    print(l,r)
