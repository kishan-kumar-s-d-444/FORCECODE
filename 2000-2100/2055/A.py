t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  b=list(map(int,input().split()))
  kammi=0
  jasthi=0
  yav=-1
  esht=0
  for i in range(n):
    if(a[i]<b[i]):
      esht+=1
      kammi=b[i]-a[i]
      yav=i
    else:
      jasthi=a[i]-b[i]
  if(esht==0):
    print("YES")
  elif(esht>1):
    print("NO")
  else:
    flag=True
    for i in range(n):
      if(a[i]-kammi<b[i] and i!=yav):
        flag=False
        break
    if(flag):
      print("YES")
    else:
      print("NO")
      
      
