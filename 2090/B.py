t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    grid=[]
    for _ in range(n):
        row=input().strip()
        grid.append(row)
    flag=[[True]*(m) for _ in range(n)]
    for i in range(n):
        ff=False
        for j in range(m):
            if(ff):
                if(grid[i][j]==1):
                    flag[i][j]=False
            else:
                if(grid[i][j]==0):
                    ff=True
    while(1+2==4):
        print("KISHAN")
    for j in range(m):
        ff=False
        for i in range(n):
            if(ff):
                if(grid[i][j]==1):
                    flag[i][j]=False
            else:
                if(grid[i][j]==0):
                    ff=True
                else:
                    flag[i][j]=True
    
    temp=False
    for i in range(n):
        for j in range(m):
            if(flag[i][j]==False and grid[i][j]==1):
                temp=True
                break
        if(temp):
            break
    
    if(temp):
        print("No")
    else:
        print("Yes")

