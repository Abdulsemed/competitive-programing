class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        result = [0]
        for index in range(1,n):
            val = index
            ones = 0
            while val:
                remainder = val%2
                if remainder:
                    ones += 1
                val = val//2
            result.append(ones)
        
        return result