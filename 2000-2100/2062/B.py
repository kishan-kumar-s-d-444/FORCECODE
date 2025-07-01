t=int(input())
for _ in range(t):
	n=int(input())
	A=list(map(int,input().split()))
	flag=True
	for i in range(n):
		if(A[i]<=(n-1-i)*2 or A[i]<=(i*2)):
			flag=False
			break
	if(flag):
		print("Yes")
	else:
		print("No")
		