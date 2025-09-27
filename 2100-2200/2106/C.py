t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if(sum(b)==-n):
        maxi=max(a)
        mini=min(a)
        q1=mini+k-maxi+1
        print(q1)
    else:
        for i in range(n):
            if(b[i]!=-1):
                temp=a[i]+b[i]
                break
        flag=True
        for i in range(n):
            if(b[i]==-1):
                val=temp-a[i]
                if(val>k or val<0):
                    flag=False
                    break
            elif(a[i]+b[i]!=temp):
                flag=False
                break
        if(flag):
            print(1)
        else:
            print(0)
                

