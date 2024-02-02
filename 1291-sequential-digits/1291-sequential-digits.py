class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        curr = 12
        val = 11
        ans = []
        count = 1
        level = "12"
        
        while curr <= high:
            if curr >= low:
                ans.append(curr)
            curr += val
            count += 1
            if str(curr)[-1:] == "0":
                val = val + (10**len(level))
                level = level + str(len(level)+1)
                curr = int(level)
                
                
        return ans
                