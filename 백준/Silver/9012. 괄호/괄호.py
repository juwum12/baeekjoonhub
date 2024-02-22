import sys
iter = int(input())
for _ in range(iter):
    string = sys.stdin.readline().strip()
    basket = []
    for ps in string:
        if basket:
            if ps == ")":
                if basket[-1] == "(":
                    basket.pop()
                else:
                    basket.append(ps)
            else:
                basket.append(ps) # )
        else:
            basket.append(ps) # 
    if len(basket) !=0 :
        print("NO")
    else:
        print("YES")
