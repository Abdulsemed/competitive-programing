class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = [0]
        for element in s:
            if element == "(":
                stack.append(element)
                result.append(0)
            else:
                if stack[-1] =="(":
                    stack.pop()
                    if result[-1] == 0:
                        result[-2] += 1
                    else:
                        result[-1] *= 2
                        result[-2] += result[-1]
                    result.pop()
                    
        return result[0]  