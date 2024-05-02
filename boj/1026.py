n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort(reverse=True)
bt=sorted(b)

result=0
for i in range(n):
    result+=a[i]*bt[i]
print(result)
