n=int(input())

for i in range(1,n+1):
	istr="#"+str(i)
	l,u,x=map(int,input().split())
	if u<x:
		print(istr,-1)
	elif l-1<x:
		print(istr,0)
	else:
		print(istr,(l-x))
