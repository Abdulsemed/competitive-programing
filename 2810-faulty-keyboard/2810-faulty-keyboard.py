class Solution:
    def finalString(self, s: str) -> str:
        ans = deque()
        flag = False
        for element in s:
            if element == "i":
                flag = not flag
            elif flag:
                ans.appendleft(element)
            else:
                ans.append(element)
        result = ("").join(ans)
        if flag:
            result = result[::-1]
        return result