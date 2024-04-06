class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        stack = []
        for element in s:
            if not stack and element != ")" and element != "(":
                ans.append(element)
            elif element != ")":
                ans.append(element)
                stack.append(element)
            elif stack:
                curr = []
                while stack and stack[-1] != "(":
                    curr.append(stack.pop())
                if stack:
                    stack.pop()
                    ans.append(")")
        curr = []
        while stack:
            
            while ans and ans[-1] != stack[-1]:
                curr.append(ans.pop())
            if stack[-1] != "(" and stack[-1] != ")":
                curr.append(stack[-1])
            ans.pop()
            stack.pop()
        ans += curr[::-1]
        return "".join(ans)      