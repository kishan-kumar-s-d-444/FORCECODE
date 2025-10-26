t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    dic=[[0,0]]
    for _ in range(n):
        a,b=map(int,input().split())
        dic.append([a,b])
    score=0
    for i in range(n):
        far=dic[i+1][0]-dic[i][0]
        if(far%2==1):
            if(dic[i+1][1]!=dic[i][1]):
                score+=far
            else:
                score+=(far-1)
        else:
            if(dic[i+1][1]==dic[i][1]):
                score+=far
            else:
                score+=(far-1)
    score+=(m-dic[n][0])
    print(score)

    