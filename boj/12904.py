import sys

input=sys.stdin.readline
a=input().rstrip()
b=input().rstrip()
bl=list(b)

while len(a)<len(bl):
    c=bl.pop()
    if c=='B':
        bl.reverse()

if a==''.join(bl):
    print(1)
else:
    print(0)
