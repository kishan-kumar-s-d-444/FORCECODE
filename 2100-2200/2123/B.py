t=int(input())
for _ in range(t):
    n,j,k=map(int,input().split())
    a=list(map(int,input().split()))
    maxi=float('-inf')
    maxind=-1
    for i in range(n):
        if(a[i]>maxi):
            maxi=a[i]
            maxind=i
        elif(a[i]==maxi and j-1==i):
            maxind=i
    if(maxind==j-1):
        print("YES")
    elif(k>1):
        print("Yes")
    else:
        print("No")

