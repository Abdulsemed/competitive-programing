class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            val = left**2 + right**2
            if val == c:
                return True
            elif val < c:
                left += 1
            else:
                right -= 1
        return False
            