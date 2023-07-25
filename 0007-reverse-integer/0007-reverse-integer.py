class Solution:
    def reverse(self, x: int) -> int:
        strs = list(str(x))
        left = 0 if strs[0] != "-"else 1
        right = len(strs)-1
        while left < right:
            strs[left], strs[right] = strs[right],strs[left]
            left += 1
            right -= 1
        val = int("".join(strs))
        if val < -2147483647 or val > 2147483647:
            return 0
        return val