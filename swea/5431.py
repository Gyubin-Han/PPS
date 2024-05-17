t=int(input())
for tc in range(1,t+1):
    n,k=map(int,input().split())
    sm=set(map(int,input().split()))
    nsm=[]
    for i in range(1,n+1):
        if not i in sm:
            nsm.append(i)
    print("#"+str(tc),*nsm)