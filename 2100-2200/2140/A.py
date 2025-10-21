from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    dic=Counter(s)
    z=0
    for i in range(dic['0']):
        if(s[i]=='0'):
            z+=1
    print(dic['0']-z)

