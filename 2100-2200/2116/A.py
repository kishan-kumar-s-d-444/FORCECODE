t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    w1=min(b,d)
    w2=min(a,c)
    if(w1<=w2):
        print("Gellyfish")
    else:
        print("Flower")
