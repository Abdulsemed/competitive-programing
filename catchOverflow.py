def overflow(lines):
    x = 0
    over = 4294967295
    stack = []
    flag = False
    for _ in range(lines):
        inp = input()
        if x > over:
            flag = True
            break
        if inp.startswith("a"):
            curr = 1
            if stack:
                for val in stack:
                    curr *= val
            x += curr
        elif inp.startswith("f"):
            stack.append(int(inp.split()[1]))
        else:
            stack.pop()
    if x > over:
        flag = True
    if not flag:
        print(x)
    else:
        print("OVERFLOW!!!")  
lines = int(input())
overflow(lines)
