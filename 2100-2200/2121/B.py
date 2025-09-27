t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    freq={}
    for c in s:
        freq[c]=freq.get(c,0)+1
    flag=False
    for i in range(1,n-1):
        if(freq[s[i]]>1):
            flag=True
            break
    if(flag):
        print("Yes")
    else:
        print("No")