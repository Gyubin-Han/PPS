n=int(input())
dont=set(['3','6','9'])

for i in range(1,n+1):
    s=str(i)

    cnt369=0
    for j in s:
        if j in dont:
            cnt369+=1

    if cnt369>0:
        for j in range(cnt369):
            print("-",end="")
        print("",end=" ")
    else:
        print(s,end=" ")