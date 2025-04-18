t=int(input())
for _ in range(t):
    p=input()
    s=input()
    n,m=len(p),len(s)
    i,j=0,0
    flag=True
    while(i<n):
        c1=1
        while(i+1<n and p[i]==p[i+1]):
            c1+=1
            i+=1
        c2=0
        while(j<m and s[j]==p[i]):
            c2+=1
            j+=1
        if(c2<c1 or c2>2*c1):
            flag=False
            break
        i+=1
    if(j!=m):
        flag=False
    if(flag):
        print("YES")
    else:
        print("No")

