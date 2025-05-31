from collections import Counter
def find(a,i,j):
    if((a[i][0]+a[j][0])%2==0):
        return 0
    elif(i>j):
        return 0
    else:
        return min(a[i][1]+find(a,i+1,j),a[j][1]+find(a,i,j-1))

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=Counter(a)
    temp=[]
    for nm,cn in count.items():
        temp.append([nm,cn])
    temp.sort()
    print(find(temp,0,len(temp)-1))

