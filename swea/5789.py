t=int(input())
for tc in range(1,t+1):
    n,q=map(int,input().split())
    d={}
    for i in range(1,n+1):
        d[i]=0
    for i in range(q):
        s,e=map(int,input().split())

        for j in range(s,e+1):
            d[j]=i+1
    rs="#"+str(tc)+" "
    for i in range(1,n+1):
        rs+=str(d[i])+" "
    print(rs)
