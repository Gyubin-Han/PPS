from queue import Queue
t=10
for _ in range(t):
    tc=int(input())
    q=Queue()
    t=list(map(int,input().split()))
    for i in t:
        q.put(i)

    isEnd=False
    while not isEnd:
        for i in range(1,5+1):
            v=q.get()-i
            if v<1:
                isEnd=True
                q.put(0)
                break
            else:
                q.put(v)
    result=[]
    while q.qsize()>0:
        result.append(q.get())
    print("#"+str(tc),*result)