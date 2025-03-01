from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count=Counter(s)
    mid=count['_']
    sid=count['-']
    if(sid%2==0):
        ans=(sid//2)*(sid//2)
    else:
        ans=(sid//2)*((sid//2)+1)
    ans=ans*mid
    print(ans)