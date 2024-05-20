t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(str,input().split()))
    narr=[]
    si=n//2
    
    for i in range(si):
        narr.append(arr[i])
        if n%2==1:
            narr.append(arr[si+i+1])
        else:
            narr.append(arr[si+i])
    if n%2==1:
        narr.append(arr[si])
    print("#"+str(tc),*narr)
