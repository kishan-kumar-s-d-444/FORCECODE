t=int(input())
for _ in range(t):
    n=int(input())
    m=n+1
    p=list(map(int,input().split()))
    q=[]
    for i in range(n):
        q.append(m-p[i])

    for i in range(n):
        print(q[i],end=" ")
        if(i==n-1):
            print("\n")
        
            
    

