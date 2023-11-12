class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for element in asteroids:
            if not stack:
                stack.append(element)
            elif (element < 0 and stack and stack[-1] < 0)  or (element > 0):
                stack.append(element)
            elif stack:
                while stack and 0 < stack[-1]  < abs(element):
                    stack.pop()
                if stack and stack[-1] == abs(element):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(element)
                
        return stack