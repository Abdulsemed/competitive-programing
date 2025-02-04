class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        index = 0
        count = 0
        while index < len(s):
            if s[index] == ")":
                if index + 1 < len(s) and s[index+1] == ")":
                    index += 1
                else:
                    count += 1
                if stack:
                    stack.pop()
                else:
                    count += 1
            else:
                stack.append("(")
            index += 1
        if stack:
            count += (len(stack)*2)

        return count