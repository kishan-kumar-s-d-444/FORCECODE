t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dic={}
    for _ in range(n):
        a,b=map(int,input().split())
        dic[a]=b
    cur=0
    at=0
    score=0
    while(1):
        if(cur in dic):
            if(dic[cur]!=at):
                at=dic[cur]
                score-=1
        if(cur==m):
            break
        at=at^1
        score+=1
        cur+=1
    print(score)
    #Time Limit 