t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=1
    prev={}
    prev_cnt=0
    flag=True
    cur={a[0]:1}
    cur_cnt=1
    for i in range(1,n):
        # print(i,"\n",prev,prev_cnt,"\n",cur,cur_cnt)
        if(flag):
            if(a[i] in cur and cur[a[i]]!=-1):
                cur[a[i]]=-1
                cur_cnt-=1
            if(a[i] not in prev or prev[a[i]]==-1):
                prev_cnt+=1
            prev[a[i]]=1
            if(cur_cnt==0):
                flag=False
                ans+=1
        else:
            if(a[i] in prev and prev[a[i]]!=-1):
                prev[a[i]]=-1
                prev_cnt-=1
            if(a[i] not in cur or cur[a[i]]==-1):
                cur_cnt+=1
            cur[a[i]]=1
            if(prev_cnt==0):
                flag=True
                ans+=1
    print(ans)

        

