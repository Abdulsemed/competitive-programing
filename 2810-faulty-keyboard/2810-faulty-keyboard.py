class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        for element in s:
            if element == "i":
                ans = ans[::-1]
                continue
            ans.append(element)
        return ("").join(ans)