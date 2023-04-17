class Solution:
    def reverseBits(self, n: int) -> int:
        arr = []
        while n:
            if n % 2 == 0:
                arr.append("0")
            else:
                arr.append("1")
            n = n//2
        
        while len(arr) < 32:
            arr.append("0")
        return int(''.join(arr),2)