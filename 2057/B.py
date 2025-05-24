t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dic={}
    q1,q2=-1,-1
    for i in a:
        dic[i]=dic.get(i,0)+1
        if(dic[i]>q2):
            q1=i
            q2=dic[i]
    dic_n= {key: val for key, val in sorted(dic.items(), key = lambda ele: ele[1], reverse = False)}
    dic_q={}
    # print(dic_n)
    for nm,cn in dic_n.items():
        if(k>0):
            if(nm!=q1):
                if(k>=cn):
                    dic_q[q1]=dic_q.get(q1,0)+cn
                    k-=cn
                else:
                    dic_q[q1]=dic_q.get(q1,0)+k
                    dic_q[nm]=dic_q.get(nm,0)+(cn-k)
                    k=0
        else:
            dic_q[nm]=dic_q.get(nm,0)+cn
    # print(dic_q)
    print(len(dic_q))
