import sys
import heapq

input = sys.stdin.readline
h=[]
arr = list(map(int,input().split()))
result = []
for i in arr:
    heapq.heappush(h,-i)
while h:
    v= heapq.heappop(h)
    print(-v)

