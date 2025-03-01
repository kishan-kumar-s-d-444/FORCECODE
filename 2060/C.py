# https://codeforces.com/problemset/problem/2060/C
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    score=0
    x.sort()
    i,j=0,n-1
    while(i<j):
        if(x[i]+x[j]==k):
            score+=1
            i+=1
            j+=1
        elif(x[i]+x[j]>k):
            j-=1
        else:
            i+=1
    print(score)
            
            
