t=int(input())

for _ in range(t):
    count=0
    x,y,n=map(int,input().split())

    while(x<=n and y<=n):
        count+=1
        if(x<y):
            x+=y
        else:
            y+=x

    print(count)
