t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    flag=False
    stack=[]
    for i in range(n//2):
        if(i+1!=n//2):
            if(s[i]==')' and s[i+1]=='('):
                flag=True

    if(flag):
        print("YES")
    else:
        print("NO")
#(()()) 
