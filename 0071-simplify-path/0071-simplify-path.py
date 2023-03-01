class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for element in path:
            if stack:
                if stack[-1] == "." and element == "/":
                    stack = self.stacking(stack)
                elif stack[-1] == "/" and element == "/":
                    continue
                stack.append(element)        
            else:
                stack.append(element)
        if stack[-1] == ".":
            stack = self.stacking(stack)
        elif len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        if len(stack) == 0:
            stack.append("/")
        return ''.join(stack)
    
    def stacking(self,stack):
        anotherOne = []
        while stack and stack[-1]  != "/":
            anotherOne.append(stack.pop())
        if len(anotherOne) >= 3:
            stack.extend(anotherOne[::-1]+[1])
        elif len(anotherOne) == 2:
            stack.pop()
            while stack and stack[-1]  != "/":
                stack.pop()
        if stack :stack.pop()
        return stack