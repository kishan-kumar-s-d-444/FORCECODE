t=int(input())
for _ in range(t):
    s=input()
    n=len(s)
    flag=False
    for i in range(n//2):
        if(s[i]==')'):
            flag=True
    if(flag):
        print("YES")
    else:
        print("NO")