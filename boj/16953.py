a,b=map(int,input().split())
count=0

while a<b:
    if b%2==0:
        b//=2
    elif b%10==1:
        b//=10
    else:
        break
    count+=1

if a==b:
    print(count+1)
else:
    print(-1)
