import sys
from collections import defaultdict
length = int(input())
city_map=[]
total =0
groups = defaultdict(int)
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]
for _ in range(length):
    city_map.append(list(sys.stdin.readline().strip()))

for row in range(length):
    for col in range(length):
        if city_map[row][col]=='0':
            continue
        city_map[row][col] ='0'
        total+=1
        groups[str(total)]+=1

        stack =[[row,col]]
        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx =x +dx[i]
                ny =y +dy[i]
                
                if nx < 0 or nx>=length or ny<0 or ny>=length or city_map[nx][ny] =='0':
                    continue
                city_map[nx][ny]='0'
                stack.append([nx,ny])
                groups[str(total)]+=1
# print(city_map)
output = list(groups.values())
output.sort()

print(total)
for o in output:
    print(o)

