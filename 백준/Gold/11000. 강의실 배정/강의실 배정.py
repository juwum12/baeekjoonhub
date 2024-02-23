import sys, heapq
from collections import defaultdict
N= int(input())
classes = []
end_times =[]
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    heapq.heappush(classes, (s,e))

heapq.heappush(end_times, heapq.heappop(classes)[1])
while classes:
    s, e = heapq.heappop(classes)
    if s < end_times[0] :
        heapq.heappush(end_times, e)
    else:
        heapq.heappop(end_times)
        heapq.heappush(end_times, e)
print(len(end_times))