t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    x1=a[0]+a[1]
    temp=[a[0],a[1],x1,a[2],a[3]]
    ans1=0
    for i in range(3):
        if(temp[i]+temp[i+1]==temp[i+2]):
            ans1+=1
    x2=a[2]-a[1]
    temp=[a[0],a[1],x2,a[2],a[3]]
    ans2=0
    for i in range(3):
        if(temp[i]+temp[i+1]==temp[i+2]):
            ans2+=1
    print(max(ans1,ans2))
