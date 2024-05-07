n=int(input())
arr=[]
mx=0

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
for i in range(n):
    v=arr[i]*(i+1)

    if mx<v:
        mx=v

print(mx)