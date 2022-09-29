def smallerNumbersThanCurrent(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums= [0]*len(nums)
        for index, num in enumerate(nums):
            for i in range(len(nums)-1):
                if nums[index] > nums[i+1]:
                    new_nums[index] += 1

        return new_nums
