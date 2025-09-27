t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    cnt=0
    one=False
    zero=False
    start=False
    for i in range(n):
        if(s[i]=='1'):
            start=True
        if(start):
            if(not one and s[i]=='1'):
                cnt+=1
                one=True
                zero=False
            if(not zero and s[i]=='0'):
                cnt+=1
                one=False
                zero=True

    print(cnt)