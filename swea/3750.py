t=int(input())
pr=[]
for tc in range(1,t+1):
    n=input()
    while len(n)>1:
        r=0
        for c in n:
            v=int(c)
            r+=v
        n=str(r)
    pr.append("#{} {}".format(tc,n))

for p in pr:
    print(p)
