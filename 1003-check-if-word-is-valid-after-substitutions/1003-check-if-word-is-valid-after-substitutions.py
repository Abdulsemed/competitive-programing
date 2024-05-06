class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element == "c":
                if len(stack) >= 2 and stack[-1] == "b" and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
                
        return not stack