class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = bin(x^y).count("1")
        return val