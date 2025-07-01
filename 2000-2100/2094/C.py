t=int(input())
for _ in range(t):
    n=int(input())
    mat=[]
    for i in range(n):
        arr=list(map(int,input().split()))
        mat.append(arr)
    m=len(mat[0])
    res=[0]
    xor=0
    for i in range(1,2*n+1):
        xor=xor^i
    for i in range(m):
        res.append(mat[0][i])
        xor=xor^mat[0][i]
    for i in range(1,n):
        res.append(mat[i][m-1])
        xor=xor^mat[i][m-1]
    res[0]=xor
    for i in res:
        print(i,end=" ")
    print("\n")