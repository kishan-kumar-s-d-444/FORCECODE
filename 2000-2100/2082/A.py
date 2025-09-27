t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for _ in range(n):
        matrix.append(input())
    rowc=0
    for i in range(n):
        o=0
        for j in range(m):
            o+=int(matrix[i][j])
        if(o%2==1):
            rowc+=1
    colc=0
    for j in range(m):
        o=0
        for i in range(n):
            o+=int(matrix[i][j])
        if(o%2==1):
            colc+=1
    print(max(rowc,colc))