class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        holder = 0
        for element in nums:
            holder += 2**element
        count = 0
        while holder:
            if holder & 1 == 0:
                return count
            count += 1
            holder >>= 1
        return count
        