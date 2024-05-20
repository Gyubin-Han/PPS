t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    dp=[1]*n
    mx=0

    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                dp[i]=max(dp[i],dp[j]+1)
            mx=max(dp[i],mx)
    print("#"+str(tc),mx)
