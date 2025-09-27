import math
t=int(input())
for _ in range(t):
    flag=True
    n=int(input())
    a=input()
    b=input()
    z1=0
    for i in range(n):
        if(i%2==0):
            if(a[i]=='0'):
                z1+=1
        else:
            if(b[i]=='0'):
                z1+=1
    if(z1>=math.ceil(n/2)):
        flag=False
    if(flag):
        print("No")
    else:
        flag=True
        z2=0
        for i in range(n):
            if(i%2==0):
                if(b[i]=='0'):
                    z2+=1
            else:
                if(a[i]=='0'):
                    z2+=1
        if(z2>=math.floor(n/2)):
            flag=False
        if(flag):
            print("No")
        else:
            print("Yes")
        
        

    

    