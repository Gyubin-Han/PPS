t=int(input())

for tc in range(1,t+1):
    a,b=map(int,input().split())

    count=0
    for i in range(a,b+1):
        v=i**(1/2)
        
        if v==int(v):
            isPal=True
            si=str(i)
            for j in range(len(si)//2):
                if not si[j]==si[-j-1]:
                    isPal=False
                    break
            vs=str(int(v))
            for j in range(len(vs)//2):
                if not vs[j]==vs[-j-1]:
                    isPal=False
                    break
            if isPal:
                count+=1
    print("#"+str(tc),count)

