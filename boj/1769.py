n=input()
count=0
r=int(n)

while len(n)>1:
    r=0
    for i in n:
        v=int(i)
        r+=v
    n=str(r)
    count+=1

print(count)
if r%3==0:
    print("YES")
else:
    print("NO")
