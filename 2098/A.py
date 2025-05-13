from collections import Counter
t=int(input())
for _ in range(t):
    s=input()
    count=Counter(s)
    res=""
    for i in range(9,-1,-1):
        print(count)
        start=i
        while(start<9 and str(start) not in count):
            start+=1
        res+=str(start)
        count[str(start)]-=1
        if(count[str(start)]==0):
            del count[str(start)]
    print(res)
