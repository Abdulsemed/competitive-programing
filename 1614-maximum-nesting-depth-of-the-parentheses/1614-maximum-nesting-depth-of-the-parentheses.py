class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        for element in s:
            if element == "(":
                stack.append("(")
            elif element != ")":
                continue
            else:
                maxim = 0
                while stack and stack[-1] != "(":
                    maxim = max(maxim,stack.pop())
                stack.pop()
                stack.append(maxim+1)
                
        return max(stack) if stack else 0