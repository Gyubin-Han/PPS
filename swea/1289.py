t=int(input())

for tc in range(1,t+1):
    s=input()
    isZero=True
    count=0

    for i in s:
        if i=='0' and not(isZero):
            isZero=True
            count+=1
        elif i=='1' and isZero:
            isZero=False
            count+=1

    print("#"+str(tc),count)
