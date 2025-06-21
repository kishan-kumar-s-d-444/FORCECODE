t=int(input())
for _ in range(t):
  n,s=map(int,input().split())
  a=map(int,input().split())
  a.sort()
  if(a[0]<s and a[n-1]>s):
      if(s-a[0]<a[n-1]-s):
        ans=2*(s-a[0])
        ans+=a[n-1]-s
      else:
        ans=2*(a[n-1]-s)
        ans+=s-a[0]
  elif(a[0]<s):
      ans=(s-a[0])
  else:
      ans=(a[n-1]-s)
  print(ans)
  
  
  
