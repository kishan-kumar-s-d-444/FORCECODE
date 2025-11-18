t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=sum(a)
    presum=0
    ans=[-1,-1]
    for l in range(n):
        presum+=a[l]
        prefix=presum%3
        midsum=0
        for r in range(l+1,n):
            midsum+=a[r]
            midfix=midsum%3
            sufsum=s-midsum-presum
            suffix=sufsum%3
            if(prefix!=midfix and midfix!=suffix and prefix!=suffix):
                ans=[l,r]
                break
            elif(prefix==midfix and midfix==suffix and prefix==suffix):
                ans=[l,r]
                break
        if(ans!=[-1,-1]):
            break
    if(ans==[-1,-1]):
        print(0,0)
    else:
        print(ans[0]+1,ans[1]+1)
