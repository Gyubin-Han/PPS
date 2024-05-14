t=10

for _ in range(t):
    tc=int(input())
    arr=[list(map(int,input().split())) for _ in range(100)]

    sum1=[0 for _ in range(100)]
    sum2=[0 for _ in range(100)]
    sumlr=0
    sumrl=0
    for i in range(100):
        for j in range(100):
            v=arr[i][j]
            sum1[i]+=v
            sum2[j]+=v

            if i==j:
                sumlr+=v
            if i-j==100-1:
                sumrl+=v

    sum1.sort()
    sum2.sort()

    mx=max(sum1[-1],sum2[-1],sumlr,sumrl)
    print("#"+str(tc),mx)
