import sys, heapq
input = sys.stdin.readline
output = []
while True :
    N = int(input())
    if N ==0:
        break
    memory = [0] * 41
    memory[1] =1
    memory[2] = 2
    
    for i in range(3,41):
        memory[i] = memory[i-2] + memory[i-1]
    output.append(memory[N])
for o in output:
    print(o)