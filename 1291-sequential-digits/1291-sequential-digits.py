class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        level = []
        val = 0
        for index in range(len(str(low))):
            level.append(str(index+1))
            val += 10**index
        level = ''.join(level)
        curr = int(level)
        while curr <= high:
            if curr >= low:
                ans.append(curr)
            curr += val
            if str(curr)[-1:] == "0":
                val = val + (10**len(level))
                level = level + str(len(level)+1)
                curr = int(level)
                
                
        return ans
                