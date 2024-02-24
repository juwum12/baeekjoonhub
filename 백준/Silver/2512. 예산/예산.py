import sys, heapq
N = int(input())
budgets = list(map(int, sys.stdin.readline().split()))
max_budget = int(input())
sum_budgets = sum(budgets)
if sum_budgets <= max_budget:
    print(sorted(budgets)[-1])
else:
    heap =[]
    for budget in budgets:
        heapq.heappush(heap, budget)

    cur_budget = max_budget
    top_budget = 0
    while heap:
        budget = heapq.heappop(heap)
        avg = cur_budget // N
        if budget > avg:
            top_budget = cur_budget //N
            break
        top_budget = budget
        cur_budget -= budget
        N -=1
    print(top_budget)