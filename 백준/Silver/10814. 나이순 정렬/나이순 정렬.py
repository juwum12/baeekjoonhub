import sys, heapq
N = int(input())
heap =[]
for i in range(N):
    age , name = sys.stdin.readline().split()
    pair = (int(age), i, name)
    heapq.heappush(heap, pair)

while heap:
    age, _, name = heapq.heappop(heap)
    print(age, name)