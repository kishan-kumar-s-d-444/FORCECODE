t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    res=[0]*(n)
    i=1
    j=n
    ind=n-1
    for k in range(n-2,-1,-1):
        if(s[k]=='<'):
            res[ind]=i
            i+=1
        else:
            res[ind]=j
            j-=1
        ind-=1
    if(j not in res):
        res[ind]=j
    else:
        res[ind]=i
    for it in res:
        print(it,end=" ")
    print("\n")

