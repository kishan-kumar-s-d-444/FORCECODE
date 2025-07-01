from collections import Counter
t=int(input())
for _ in range(t):
    s=input()
    count=Counter(s)
    print(count['1'])