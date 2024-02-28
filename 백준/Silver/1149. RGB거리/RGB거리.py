import sys, copy
input = sys.stdin.readline
N = int(input())
NUM_COLOR = 3
homes =[]
memory =[[0]*3 for _ in range(N)]
for _ in range(N):
    homes.append(list(map(int, input().split())))

for i, home in enumerate(homes):
    if i ==0:
        memory[0] = copy.deepcopy(homes[0]) 
        continue
    for j in range(NUM_COLOR):
        minimum = 1000*1000
        for k in range(NUM_COLOR):
            if j==k:
                continue
            
            minimum = min(minimum, homes[i][j] + memory[i-1][k])
        memory[i][j] = minimum
print(min(memory.pop()))