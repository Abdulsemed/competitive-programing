class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = []
        for element in tokens:
            if element not in ("+-/*"):
                stack.append(int(element))
            else:
                if element == "+":
                    stack[-2]= stack[-2] + stack[-1]
                elif element == "-":
                    stack[-2]= stack[-2] - stack[-1]
                elif element == "/":
                    stack[-2]= int(stack[-2] / stack[-1])
                else:
                    stack[-2]= stack[-2] * stack[-1]
                stack.pop()
        return stack[0]
                    
            