t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    q1=float('-inf')
    q2=float('-inf')
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]>q1):
                q1=matrix[i][j]
            elif(matrix[i][j]==q1):
                q2=matrix[i][j]
            elif(matrix[i][j]>q2):
                q2=matrix[i][j]
    q1-=1
    print(max(q1,q2))