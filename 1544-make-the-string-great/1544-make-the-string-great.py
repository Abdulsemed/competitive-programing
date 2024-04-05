class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for element in s:
            if stack and stack[-1].lower() == element.lower() and (element.isupper() and stack[-1].islower() or stack[-1].isupper() and element.islower()):
                stack.pop()
            else:
                stack.append(element)
                
        return "".join(stack)