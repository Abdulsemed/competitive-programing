def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > 0 and len(nums) > 1:
            k = k % len(nums)
            beg = 0
            end = len(nums)-1
            result = [0]*len(nums)
            while beg <= end :
                result[(beg+k)%len(nums)] = nums[beg]
                beg+=1
            nums[:] = result
