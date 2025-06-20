t=int(input())
for _ in range(t):
  n,s=map(int,input().split())
  a=map(int,input().split())
  a.sort()
  if(s-a[0]<a[n-1]-s):
    ans=2*(s-a[0])
    ans+=a[n-1]-s
  else:
    ans=2*(a[n-1]-s)
    ans+=s-a[0]
  print(ans)
  
  
  
