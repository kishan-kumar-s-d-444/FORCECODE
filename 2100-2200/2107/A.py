t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    odd=[]
    even=[]
    for i in range(n):
        if(a[i]%2==1):
            odd.append(a[i])
        else:
            even.append(a[i])
    if(not odd):
        flag=True
        for i in range(n-1):
            if(even[i]!=even[i+1]):
                flag=False
                break
        if(flag):
            print("No")
        else:
            temp=False
            print("Yes")
            for i in range(n):
                if(a[i]==2):
                    print(2,end=" ")
                else:
                    if(temp):
                        print(2,end=" ")
                    else:
                        print(1,end=" ")
                        temp=True
            print(" ")
    elif(not even):
        flag=True
        for i in range(n-1):
            if(odd[i]!=odd[i+1]):
                flag=False
                break
        if(flag):
            print("No")
        else:
            temp=False
            print("Yes")
            for i in range(n):
                if(a[i]==1):
                    print(2,end=" ")
                else:
                    if(temp):
                        print(2,end=" ")
                    else:
                        print(1,end=" ")
                        temp=True
            print(" ")
    else:
        print("Yes")
        for i in range(n):
            if(a[i] in odd):
                print(2,end=" ")
            else:
                print(1,end=" ")
        print(" ")

