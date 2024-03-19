import sys, math
input = sys.stdin.readline
iter = int(input())

results = []
for _ in range(iter):
    start, end = map(int, input().split())
    d = end - start
    if d <= 3:
        results.append(d)
        continue
    
    n = int(d**(1/2))
    n_squared = n ** 2
    execution = (2*n)-1
    if d == n_squared :
        results.append(execution)
    elif d <= n + n_squared:
        results.append(execution+1)
    else:
        results.append(execution+2)
for result in results:
    print(result)
    
