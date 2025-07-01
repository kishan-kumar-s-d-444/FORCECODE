t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dic={0:3,1:1,2:2,3:1,5:1}
    
    ans=0
    for  i in range(n):
        if(a[i] in dic):
            dic[a[i]]-=1
            if(dic[a[i]]==0):
                del dic[a[i]]
        if(not dic):
            ans=i+1
            break
    print(ans)