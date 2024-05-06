da=set(['a','e','i','o','u'])

t=int(input())

for tc in range(1,t+1):
    s=input()
    result=""

    for i in s:
        if not i in da:
            result+=i
    print("#"+str(tc),result)

