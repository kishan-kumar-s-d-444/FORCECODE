t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if((a+b+c)%3==0 and (a+b+c)//3>=b and (a+b+c)//3>=a):
        print("YES")
    else:
        print("No")