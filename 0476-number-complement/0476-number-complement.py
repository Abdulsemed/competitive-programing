class Solution:
    def findComplement(self, num: int) -> int:
        ans = []
        while num:
            rem = num % 2
            if rem:
                ans.append("0")
            else:
                ans.append("1")
            num = num//2
        ans.append("b")
        ans.append("0")
        val = int(''.join(ans[::-1]),2)
        return val