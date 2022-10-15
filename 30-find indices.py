def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for index in range(len(nums)-1):
            j = index
            for i in range(index+1, len(nums)):
                if nums[j] > nums[i]:
                    j = i
                    
            if j != index:
                (nums[index], nums[j]) = (nums[j], nums[index]) 
                
            if nums[index] == target:
                result.append(index)
        if nums[len(nums)-1] == target:
                result.append(len(nums)-1)
        return result
