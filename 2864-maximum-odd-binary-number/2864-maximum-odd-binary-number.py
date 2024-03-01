class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        return "".join(sorted(s,reverse = True)[1:] + ["1"])