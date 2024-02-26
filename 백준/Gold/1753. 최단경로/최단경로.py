import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
V, E = map(int, input().split())
start_node = int(input())
inf = int(1e9)

graph = [[] for _ in range(V+1)]
for _ in range(E):
    node, adj, d = map(int, input().split())
    graph[node].append((adj, d))

dist = [inf] * (V+1)
q = []
heapq.heappush(q, (0, start_node))
dist[start_node] = 0

while q:
    d, node = heapq.heappop(q)
    
    if d > dist[node]:
        continue
    
    for adj, d in graph[node]:
        cost = d + dist[node]
        if cost < dist[adj]:
            dist[adj] = cost
            heapq.heappush(q, (cost, adj))

for d in dist[1:]:
    if d == inf:
        print("INF")
    else:
        print(d)