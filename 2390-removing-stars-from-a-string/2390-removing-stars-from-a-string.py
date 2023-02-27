class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for element in s:
            if element != "*":
                stack.append(element)
            else:
                stack.pop()
        return ''.join(stack)