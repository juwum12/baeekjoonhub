import sys
n = int(input())
consumers = sorted(map(int, sys.stdin.readline().split()))
result = 0
for consumer in consumers:
    result += consumer * n
    n-=1
    
print(result)