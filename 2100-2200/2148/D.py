t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    oddmax=[]
    for kis in a:
        if(kis%2==1):
            oddmax.append(kis)
    if(not oddmax):
        print(0)
    else:
        even=sum(a)-sum(oddmax)
        oddmax.sort()
        even+=sum(oddmax[len(oddmax)//2:])
        print(even)