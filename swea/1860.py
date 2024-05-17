from queue import Queue
t=int(input())
for tc in range(1,t+1):
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    q=Queue()
    arr.sort()
    for i in arr:
        q.put(i)

    isPos=True
    time=1
    cnt=0
    last=q.get()
    while isPos and not(last<time):
        if time%m==0:
            cnt+=k
        while last==time:
            cnt-=1
            if q.qsize()>0:
                last=q.get()
            else:
                last=-1
            if cnt<0:
                isPos=False
                break
        time+=1
    if last==0:
        isPos=False
    isPosStr=""
    if isPos:
        isPosStr="Possible"
    else:
        isPosStr="Impossible"
    print("#"+str(tc),isPosStr)
