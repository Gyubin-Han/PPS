t=int(input())
for tc in range(1,t+1):
    isCo=True
    c=set()
    d={}
    p=input()
    pl=len(p)//3
    for i in range(pl):
        v=p[i*3:i*3+3]
        if v in c:
            isCo=False
            break
        c.add(v)
        d[v[0]]=d.get(v[0],0)+1 

    if not isCo:
        print("#"+str(tc),"ERROR")
        continue
    cs=13-d.get('S',0)
    cd=13-d.get('D',0)
    ch=13-d.get('H',0)
    cc=13-d.get('C',0)

    print("#"+str(tc),cs,cd,ch,cc)
