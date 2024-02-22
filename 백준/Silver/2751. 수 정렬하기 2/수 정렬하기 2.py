import sys, heapq
N= int(input())
heap =[]
for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))

while heap:
    print(heapq.heappop(heap))