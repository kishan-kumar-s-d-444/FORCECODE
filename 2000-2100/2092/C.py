t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    even=[]
    odd=[]
    for i in range(n):
        if(a[i]%2==0):
            even.append(a[i])
        else:
            odd.append(a[i])
    if(not even):
        print(max(odd))
    elif(not odd):
        print(max(even))
    else:
        even.sort()
        odd.sort()
        ans=odd.pop()
        while(odd):
            q1=odd.pop()
            if(q1>1):
                ans+=(q1-1)
        ans+=(sum(even))
        print(ans)


    