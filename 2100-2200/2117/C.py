t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    ans+=1
    prev=set()
    prev_cnt=0
    flag=True
    cur=set()
    cur.add(a[0])
    cur_cnt=0
    cur_cnt+=1
    for i in range(1,n):
        if(flag):
            if(a[i] in cur):
                cur.remove(a[i])
                cur_cnt-=1
            if(a[i] not in prev):
                prev_cnt+=1
                prev.add(a[i])
            if(cur_cnt==0):
                flag=False
                ans+=1
        else:
            if(a[i] in prev):
                prev.remove(a[i])
                prev_cnt-=1
            if(a[i] not in cur):
                cur_cnt+=1
                cur.add(a[i])
            if(prev_cnt==0):
                flag=True
                ans+=1
    print(ans)

        
