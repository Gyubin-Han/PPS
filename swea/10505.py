t=int(input())

for i in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    
    s=0
    sarr=set()
    cnt={}
    for j in range(n//2):
        a,b=arr[j],arr[-j-1]
        s+=a+b
        sarr.add(a)
        sarr.add(b)
        if a in cnt:
            cnt[a]+=1
        else:
            cnt[a]=1
        if b in cnt:
            cnt[b]+=1
        else:
            cnt[b]=1
    if n%2==1:
        a=arr[n//2]
        s+=a
        sarr.add(a)
        if a in cnt:
            cnt[a]+=1
        else:
            cnt[a]=1

    avg=s//n
    result=0
    slist=list(sarr)
    slist.sort()
    for j in slist:
        if j>avg:
            break
        result+=cnt[j]
    
    print("#"+str(i),result)
