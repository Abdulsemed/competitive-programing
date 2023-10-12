class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = x
        result = 1
        k = abs(n)
        while k:
            if k & 1:
                result = result * power
            power = power * power
            k >>= 1
        if n < 0:
            result = 1 / result
        return result
            