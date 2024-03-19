import sys
while True:
    string = sys.stdin.readline()
    stack = []
    if string == ".\n":
        break
    else:
        for s in string:
            if s == "(" or s == "[":
                stack.append(s)
            elif s == ")":
                if stack:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(s)
                        break
                else:
                    stack.append(s)
                    break
            elif s == "]":
                if stack:
                    if stack[-1] == "[": # "]hello"
                        stack.pop()
                    else:
                        stack.append(s)
                        break
                else:
                    stack.append(s)
                    break
    if stack:
        print('no')
    else:
        print('yes')