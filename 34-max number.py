def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        beg = 0
        end = len(nums) - 1
        while beg < end:
            if nums[beg] + nums[end] == k:
                count += 1
                beg += 1
                end -= 1
            elif nums[beg] + nums[end] < k:
                beg += 1
            else:
                end -= 1
        return count
