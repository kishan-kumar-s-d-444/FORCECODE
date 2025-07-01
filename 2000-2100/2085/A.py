t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    if(n==1):
        print("No")
    else:
        r=s[::-1]
        if(s<r):
             print("Yes")
        else:
             if(k==0):
                 print("No")
             else:
                 flag=False
                 v=s[0]
                 for i in range(1,n):
                     if(s[i]<v):
                         flag=True
                         break
                 if(not flag):
                     v=s[n-1]
                     for i in range(n-2,-1,-1):
                         if(s[i]>v):
                             flag=True
                             break
                 if(flag):
                     print("Yes")
                 else:
                     print("No")