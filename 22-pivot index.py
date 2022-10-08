 def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = -1
        if sum(nums[1:]) == 0:
            return 0
        left_sum = [nums[0]]
        right_sum = [nums[-1]]
        for index in range(len(nums)-3):
            left_sum.append(nums[index+1]+left_sum[index])
            right_sum.append(nums[len(nums)-2-index]+right_sum[index])
        right_sum = right_sum[::-1]
        for index in range(len(left_sum)):
            if left_sum[index] == right_sum[index]:
                return index+1

        if sum(nums[:len(nums)-1]) == 0:
            pos = len(nums)-1
        return pos
