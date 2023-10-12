class Solution:
    def multiply(self, a, b, m):
        return ((a % m) * (b % m)) % m

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
    def countGoodNumbers(self, n: int) -> int:
        odd = 4
        even = 5
        mod = 10**9+7
        if n == 1:
            return even
        
        if n % 2:
            n = n//2
            result = self.multiply(pow(odd,n,mod), pow(even,n+1,mod), mod) 
        else:
            n = n//2
            result = self.multiply(pow(odd,n,mod), pow(even,n,mod), mod) 
            
        return result % mod
        