t=int(input())

for tc in range(1,t+1):
    a,b=map(int,input().split())
    
    result=0
    if a>9 or b>9:
        result=-1
    else:
        result=a*b

    print("#"+str(tc),result)
