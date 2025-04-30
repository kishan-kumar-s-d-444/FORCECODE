t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    st,en=-1,-1
    for i in range(n):
        if(s[i]=='0'):
            if(st==-1):
                st=i
            en=i
        elif(st!=-1 and s[i]=='1'):
            break
    if(st==-1):
        print(n+1)
    elif(en-st+1==n):
        print(n)
    else:
        temp=s[:(en+1)][::-1]
        temp+=s[(en+1):]
        cnt=0
        flag=False
        for i in range(n):
            if(temp[i]=='0'):
                if(flag):
                    cnt+=1
                    flag=not flag
                cnt+=1
            else:
                if(not flag):
                    cnt+=1
                    flag=not flag
                cnt+=1
        print(cnt)

    