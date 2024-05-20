t=int(input())
for tc in range(1,t+1):
    arr=[]
    s=""
    mx=0
    for i in range(5):
        arr.append(list(input()))
        mx=max(len(arr[-1]),mx)
    for i in range(mx):
        for j in range(5):
            if len(arr[j])>i:
                s+=arr[j][i]
    print("#"+str(tc),s)
