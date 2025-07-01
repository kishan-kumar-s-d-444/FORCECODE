t=int(input())
for _ in range(t):
    n=int(input())
    ans=0
    q1=0
    ind=1
    for i in range(n,0,-1):
        q1+=abs(i-ind)
        ind+=1
    print(q1//2+1)