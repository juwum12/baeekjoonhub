import sys, heapq
iter=int(input())
output = []
for _ in range(iter):
    N = int(input())
    grade =[]

    for _ in range(N):
        doc, interview = map(int, sys.stdin.readline().split())
        heapq.heappush(grade, (doc, interview))
        
    d, i = heapq.heappop(grade)
    max_interview = i
    count = 1
    while grade:
        d, i = heapq.heappop(grade)
        if i < max_interview:
            max_interview = i
            count+=1
    output.append(count)
for o in output:
    print(o)