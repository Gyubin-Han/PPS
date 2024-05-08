t=int(input())

for _ in range(1,t+1):
    tc=int(input())
    arr=list(map(int,input().split()))
    cnt={}
    mx=(0,0)

    for i in arr:
        if i in cnt:
            cnt[i]+=1
        else:
            cnt[i]=1

        if cnt[i]>mx[1] or (cnt[i]==mx[1] and i>mx[0]):
            mx=(i,cnt[i])
    print("#"+str(tc),mx[0])
