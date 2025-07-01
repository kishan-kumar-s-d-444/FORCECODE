t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    dic={'0':0,'1':0}
    for c in s:
        dic[c]+=1
    flag=False
    while(k):
        if(dic['0']>dic['1']):
            zero=True
        else:
            zero=False
        if(zero):
            if(dic['0']>1):
                dic['0']-=2
            else:
                flag=True
                break
        else:
            if(dic['1']>1):
                dic['1']-=2
            else:
                flag=True
                break
        k-=1
    # print(dic)
    if(flag):
        print("NO")
    else:
        if(dic['0']==dic['1']):
            print("YES")
        else:
            print("NO")

    
    