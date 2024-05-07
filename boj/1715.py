import sys
from queue import PriorityQueue
input=sys.stdin.readline
n=int(input().rstrip())
pq=PriorityQueue()

for _ in range(n):
    pq.put(int(input().rstrip()))

l=[]
while pq.qsize()>1:
    a=pq.get()
    b=pq.get()
    pq.put(a+b)
    l.append(a+b)

while len(l)>1:
    a=l.pop()
    b=l.pop()
    l.append(a+b)

if len(l)==0:
    print(0)
else:
    print(l.pop())
