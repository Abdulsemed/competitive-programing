class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinctSet = set(tuple(nums))
        nums[:] = list(map(str,nums))
        count = len(distinctSet)
        if count == 1:
            if int(nums[0][::-1]) == int(nums[0]):
                return 1
            else:
                return 2
        else:
            for element in nums:
                val = int(element[::-1])
                if val not in distinctSet:
                    distinctSet.add(val)
                    count += 1
        
        return count
            
        