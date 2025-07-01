t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dic={}
    for i in range(n):
        if(a[i] not in dic):
            dic[a[i]]=1
    print(len(dic))