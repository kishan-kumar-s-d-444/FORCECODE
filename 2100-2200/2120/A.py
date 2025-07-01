t=int(input())
for _ in range(t):
    l1,b1,l2,b2,l3,b3=map(int,input().split())
    if(l1==l2==l3 and b1+b2+b3==l1):
        print("Yes")
    elif(l1==l2+l3 and b2==b3 and b1+b2==l1):
        print("Yes")
    elif(b1==b2==b3 and l1+l2+l3==b1):
        print("Yes")
    elif(b1==b2+b3 and l2==l3 and l1+l2==b1):
        print("Yes")
    else:
        print("No")
     