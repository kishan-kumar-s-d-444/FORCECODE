t=int(input())
for _ in range(t):
    n=int(input())
    res=0
    for i in range(n):
        a,b,c,d=map(int,input().split())
        if(b>d):
            res+=(b-d)
            res+=a
        else:
            res+=max(0,a-c)

    # for i in range(n):
    #     if(flag[i]==0):
    #         if(arr[i][1]>arr[i][3]):
    #             res+=(arr[i][1]-arr[i][3])
    #             res+=arr[i][0]
    #         elif(arr[i][0]>arr[i][2]):
    #             res+=(arr[i][0]-arr[i][2])
    print(res)

# 3
# 0 1 2 0
# 2 0 1 2
# 1 2 0 1