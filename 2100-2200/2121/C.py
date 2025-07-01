from collections import defaultdict
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    matrix=[]
    for _ in range(n):
        matrix.append(list(map(int,input().split())))
    q1=float('-inf')
    temp1=[]
    temp2=[]
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]>q1):
                q1=matrix[i][j]
                temp1=[]
                temp2=[]
            if(matrix[i][j]==q1):
                temp1.append([i,j])
                temp2.append([i,j])
    flag1=True
    n1=len(temp1)
    col1=-1
    for i in range(1,n1):
        if(temp1[i][0]==temp1[0][0]):
            continue
        elif(col1==-1):
            col1=temp1[i][1]
        elif(col1==temp1[i][1]):
            continue
        else:
            flag1=False
            break
    
    flag2=True
    n2=len(temp2)
    row2=-1
    for i in range(1,n2):
        if(temp2[i][1]==temp2[0][1]):
            continue
        elif(row2==-1):
            row2=temp2[i][0]
        elif(row2==temp2[i][0]):
            continue
        else:
            flag2=False
            break
    if(flag1 or flag2):
        print(q1-1)
    else:
        print(q1)
    