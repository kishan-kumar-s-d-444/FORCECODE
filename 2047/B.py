from collections import Counter
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    count=Counter(s)
    mch,mcn='',float('-inf')
    sch,scn='',float('inf')
    for ch,cn in count.items():
        if(cn>mcn):
            mcn=cn
            mch=ch
        if(cn<scn):
            scn=cn
            sch=ch
        elif(cn==scn and ch!=mch):
            sch=ch
    res=""
    flag=False
    for c in s:
        if(c==sch and flag==False):
            flag=True
            res+=mch
        else:
            res+=c
    print(res)

    
