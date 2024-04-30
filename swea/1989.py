t=int(input())

for i in range(1,t+1):
    s=input()
    
    rFlag=True
    for j in range(len(s)//2):
        if not s[j]==s[-j-1]:
            rFlag=False
            break

    if rFlag:
        print("#"+str(i),1)
    else:
        print("#"+str(i),0)
