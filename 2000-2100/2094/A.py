t=int(input())
for _ in range(t):
    s=input()
    temp=s.split(' ')
    res=""
    for it in temp:
        res+=it[0]
    print(res)