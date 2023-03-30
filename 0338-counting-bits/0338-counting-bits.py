class Solution:
    def countBits(self, n: int) -> List[int]:
        n += 1
        result = []
        curr = 0
        print(curr)
        for index in range(n):
            count = 0
            val = curr
            while val:
                if val & 1:
                    count += 1
                val = val>>1
            curr += 1
            result.append(count)
        return result