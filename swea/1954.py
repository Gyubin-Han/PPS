t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    count=1
    x=0
    y=0
    lim=n-1
    limcnt=0
    isXy=True

    while count<(n*n)+1:
        arr[abs(y)][abs(x)]=count
        if limcnt==lim:
            if isXy:
                x*=-1
                lim-=1
            else:
                y*=-1
            isXy=not(isXy)
            limcnt=0
        else:
            limcnt+=1
        if isXy:
            x+=1
        else:
            y+=1
        count+=1

    print("#"+str(tc))
    for a in arr:
        print(*a)