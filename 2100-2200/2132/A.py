t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    m=int(input())
    b=input()
    c=input()
    for i in range(m):
        if(c[i]=='V'):
            a=b[i]+a
        else:
            a=a+b[i]
    print(a)

     

