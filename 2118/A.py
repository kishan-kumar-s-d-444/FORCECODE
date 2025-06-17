t=int(input())
for _ in range(t):
  n,k=map(int,input().split())
  res='1'*(k)
  res=res+'0'*(n-k)
  print(res)

