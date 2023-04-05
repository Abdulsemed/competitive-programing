class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        val = 1
        ans = 0
        for index in range(32):
            val = 1<<index 
            count = 0
            for num in nums:
                if num & val:
                    count += 1
            if count % 3:
                ans += 2**index
        count = 0
        for num in nums:
            if num < 0:
                count += 1
                
        if count % 3:
            ans = ans - (1<<32)
            
        return ans
            