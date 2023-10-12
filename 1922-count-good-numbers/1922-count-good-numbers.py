class Solution:
    def multiply(self, a, b, m):
        return ((a % m) * (b % m)) % m

    def myPow(self, x: float, n: int, m) -> float:
        power = x
        result = 1
        k = abs(n)
        while k:
            if k & 1:
                result = self.multiply(result, power,m)
            power = self.multiply(power,power,m)
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
            result = self.multiply(self.myPow(odd,n,mod), self.myPow(even,n+1,mod), mod) 
        else:
            n = n//2
            result = self.multiply(self.myPow(odd,n,mod), self.myPow(even,n,mod), mod) 
            
        return result % mod
        