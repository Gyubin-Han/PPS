s=input()

count=0
last=s[0]
for i in range(1,len(s)):
    if not s[i]==last:
        count+=1
        last=s[i]
if count%2==1:
    print(count//2+1)
else:
    print(count//2)
