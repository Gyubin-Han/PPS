import sys
input=sys.stdin.readline
n=int(input().rstrip())
arr=list(map(int,input().rstrip().split()))

last=0
result=0
for i in range(1,n+1):
    if arr[-i]>last:
        last+=1
    elif arr[-i]<last:
        last=arr[-i]
    result+=last
print(result)
