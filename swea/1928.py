# 이 문제를 별도의 모듈을 사용하지 않고 해결
base64Table="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64Dict={}
for i in range(len(base64Table)):
	c=base64Table[i]
	base64Dict[c]=i

n=int(input())

for i in range(1,n+1):
	s=input()

	buffer=0
	count=0
	resultString=""
	for c in s:
		buffer=(buffer<<6)|base64Dict[c]
		count+=6

		if count>=8:
			count-=8
			resultString+=chr((buffer>>count)&0xff)
			buffer&=(1<<count)-1
	print("#"+str(i),resultString)
