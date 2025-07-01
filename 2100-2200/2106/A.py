t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    c=0
    for i in range(n):
        for j in range(n):
            if(i==j):
                if(s[j]=='0'):
                    c+=1
            else:
                if(s[j]=='1'):
                    c+=1
    print(c)
