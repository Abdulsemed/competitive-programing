 def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            beg = 0
            end = 0
            while end <= len(nums)-1:
                if nums[beg] == 0:
                    nums.append(nums[beg])
                    nums.pop(beg)
                else:
                    beg += 1
                end += 1
