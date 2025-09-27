t=int(input())
for _ in range(t):
    x,k=map(int,input().split())
    if(x==1):
        if(k==1):
            print("No")
        elif(k==2):
            print("Yes")
        else:
            print("No")
    else:
        flag=True
        for i in range(2,int(x**0.5)+1):
            if(x%i==0):
                flag=False
                break
        if(flag and k==1):
            print("YES")
        else:
            print("NO")
