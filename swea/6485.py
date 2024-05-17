t=int(input())

for tc in range(1,t+1):
    n=int(input())
    bs={}

    for i in range(n):
        s,e=map(int,input().split())
        for j in range(s,e+1):
            if j in bs:
                bs[j]+=1
            else:
                bs[j]=1
    p=int(input())
    result=[]
    for i in range(p):
        po=int(input())
        
        if po in bs:
            result.append(bs[po])
        else:
            result.append(0)
    print("#"+str(tc),*result)
