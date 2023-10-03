class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for letter in s:
            
            if stack:
                if stack[-1][0] == letter:
                    stack[-1][1] += 1
                else:
                    stack.append([letter,1])
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([letter, 1])
                
        ans = []
        for key,val in stack:
            for _ in range(val):
                ans.append(key)
            
        return "".join(ans)