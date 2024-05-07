s=input()

smarr=s.split("-")
front=True
result=0

for i in smarr:
    p=0
    for j in i.split("+"):
        p+=int(j)
    if front:
        result+=p
        front=False
    else:
        result-=p

print(result)