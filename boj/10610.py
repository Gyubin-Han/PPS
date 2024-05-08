n=input()
narr=[]

for i in n:
    narr.append(int(i))
narr.sort(reverse=True)

s=narr[0]
for i in range(1,len(narr)):
    s*=10
    s+=narr[i]

if s%30==0:
    print(s)
else:
    print(-1)
