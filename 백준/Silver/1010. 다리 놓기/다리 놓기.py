import sys, math
intput = sys.stdin.readline

iter = int(input())
results = []
for _ in range(iter):
    N, M = map(int, input().split())
    answer = math.comb(M,N)
    results.append(answer)

for result in results:
    print(result)