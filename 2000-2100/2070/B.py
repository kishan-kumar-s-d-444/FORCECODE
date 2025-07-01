t=int(input())
for _ in range(t):
    n,x,k=map(int,input().split())
    flag=False
    s=input()
    t1=0
    for c in s:
        if(t1>=k):
            break
        if(c=='L'):
            x-=1
        else:
            x+=1
        t1+=1
        if(x==0):
            flag=True
            break
    if(flag):
        x=0
        flag=False
        t2=0
        for c in s:
            if(t1+t2>=k):
                break
            if(c=='L'):
                x-=1
            else:
                x+=1
            t2+=1
            if(x==0):
                flag=True
                break
        if(flag):
            tot=2
            k1=k-t1-t2
            tot+=(k1//t2)
            print(tot)
        else:
            print(1)
    else:
        print(0)
    

        
    