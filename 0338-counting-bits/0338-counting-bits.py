class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        result = []
        for index in range(n):
            count = Counter(bin(index))
            result.append(count["1"])
        
        return result