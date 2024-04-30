n,k=map(int,input().split())
oarr=[]
for i in range(n):
    oarr.append(int(input()))

oarr.reverse()

count=0
for i in oarr:
    d=int(k/i)
    k-=(i*d)
    count+=d

print(count)
