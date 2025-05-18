t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=True
    for i in range(n-1):
        if(a[i]==0 and a[i+1]==0):
            flag=False
            break
    if(not flag):
        print("Yes")
    else:
        flag=True
        if(a[0]==1):
            for i in range(n):
                if(a[i]==0):
                    flag=False
                    break
        else:
            flag=False
        if(flag):
            print("Yes")
        else:
            print("No")
                    

    

            
