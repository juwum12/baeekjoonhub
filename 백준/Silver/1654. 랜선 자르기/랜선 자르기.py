import sys
N, K = map(int, input().split())
mylines=[]
for _ in range(N):
    mylines.append(int(sys.stdin.readline()))
start = 1
end = max(mylines)
max_length =0
while start <= end:
    cnt=0
    mid = max((start+end) // 2, 1)
    for line in mylines:
        cnt += line // mid
        
    if cnt >= K:
        max_length = mid
        start = mid+1
    else:
        end = mid-1
print(max_length)