def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for index in range(len(tokens)):
            if tokens[index].isnumeric() or tokens[index].lstrip('-').isnumeric():
                stack.append(int(tokens[index]))

            else:
                max_index = len(stack)
                if tokens[index] == "/":
                    if (stack[max_index - 2] // stack[max_index - 1]) >= 0:
                        stack[max_index-2] = stack[max_index - 2] // stack[max_index - 1]
                    elif (stack[max_index - 2] % stack[max_index - 1]) != 0:
                        stack[max_index - 2] = (stack[max_index - 2] // stack[max_index - 1])+1
                    else:
                        stack[max_index - 2] = (stack[max_index - 2] // stack[max_index - 1])
                elif tokens[index] == "*":
                    stack[max_index - 2] = stack[max_index - 2] * stack[max_index - 1]
                elif tokens[index] == "+":
                    stack[max_index - 2] = stack[max_index - 2] + stack[max_index - 1]
                elif tokens[index] == "-":
                    stack[max_index - 2] = stack[max_index - 2] - stack[max_index - 1]
                if (len(stack) > 1):
                    stack.pop()
                    
        return stack[0]
