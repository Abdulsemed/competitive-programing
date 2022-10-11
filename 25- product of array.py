def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p_asc = [nums[0]]
        p_dsc = [nums[len(nums)-1]]*(len(nums))
        p_arr = []
        index = len(nums)-1
        top = index
        while index > 0:
            p_asc.append(p_asc[top-index]*nums[top-index+1])
            p_dsc[index-1] = p_dsc[index]*nums[index-1]
            index -= 1
        for index in range(len(nums)):
            if index == 0:
                p_arr.append(p_dsc[1])
            elif index == top:
                p_arr.append(p_asc[top-1])
            else:
                p_arr.append(p_asc[index-1]*p_dsc[index+1])
        
        return p_arr
