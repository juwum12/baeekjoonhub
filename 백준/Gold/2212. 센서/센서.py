import sys
n= int(input())
k = int(input())
sensors = map(int, sys.stdin.readline().split())
sensors = sorted(set(sensors))
distance = []
for i in range(len(sensors)-1):
    d = sensors[i+1] - sensors[i]
    distance.append(d)
distance.sort()
print(sum(distance[:len(sensors)-k]))