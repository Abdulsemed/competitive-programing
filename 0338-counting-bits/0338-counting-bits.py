class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        result = [0,1] if n > 1 else [0]
        for index in range(2,n):
            if index % 2 == 0:
                result.append(result[index//2])
            else:
                result.append(result[index//2]+1)
        return result