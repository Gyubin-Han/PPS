t=int(input())

for i in range(1,t+1):
	n=int(input())
	arr=[0 for _ in range(5)]
	
	while not n<2:
		if n%2==0:
			arr[0]+=1
			n/=2
		elif n%3==0:
			arr[1]+=1
			n/=3
		elif n%5==0:
			arr[2]+=1
			n/=5
		elif n%7==0:
			arr[3]+=1
			n/=7
		else:
			arr[4]+=1
			n/=11
	print("#"+str(i),*arr)
