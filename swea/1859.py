t=int(input())

for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))

    mx=0
    r=0
    for i in range(1,n+1):
        if arr[-i]>mx:
            mx=arr[-i]
        else:
            r+=mx-arr[-i]
    print("#"+str(tc),r)
