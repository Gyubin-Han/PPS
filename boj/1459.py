import sys
input=sys.stdin.readline

x,y,tw,ts=map(int,input().rstrip().split())
tw2=tw*2
ts2=ts*2
sum=0

minxy=min(x,y)
if minxy>0:
    sum+=(min(ts,tw2)*minxy)
    x-=minxy
    y-=minxy

maxxy=max(x,y)
if maxxy>0:
    if (maxxy%2)==0:
        sum+=(min(ts2,tw2)*int(maxxy/2))
    elif maxxy>2:
        sum+=(min(ts2,tw2)*int(maxxy/2)+tw)
    else:
        sum+=tw

print(sum)
