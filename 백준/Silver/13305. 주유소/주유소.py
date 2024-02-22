import sys
N= int(input())
d = list(map(int, sys.stdin.readline().split()))
city = list(map(int, sys.stdin.readline().split()))
oil = 0
cost = 0
for i in range(len(d)):
    if i==0:
        cost += d[i] * city[i]
        oil = city[i]
        continue
    if city[i] > oil :
        cost += oil * d[i]
        continue
    else:
        oil = city[i]
        cost += oil * d[i]
print(cost)