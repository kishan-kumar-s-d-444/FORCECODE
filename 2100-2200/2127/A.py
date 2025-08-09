t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=True
    for i in range(n-2):
        maxi=float('-inf')
        mini=float('inf')
        if(-1 in a[i:i+3]):
            continue
        for j in range(i,i+3):
            if(a[j]!=-1):
                maxi=max(maxi,a[j])
                mini=min(mini,a[j])
        if(maxi==float('inf')):
            continue
        for j in range(max+2):
            if(j not in a[i:i+3]):
                mex=j
        if(mex!=maxi-mini):
            flag=False
            break
    if(flag):
        print("yes")
    else:
        print("No")