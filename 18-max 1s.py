def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) > 1:
            beg = 0
            end = 0
            zeroes = 0
            count = 0
            max_length = 0
            while beg < len(nums) and end < len(nums):
                if nums[end] == 1 and zeroes <= k:
                    count += 1
                    end += 1
                elif nums[end] == 0 and zeroes < k:
                    zeroes += 1
                    end += 1
                else:
                    if nums[beg] == 1:
                        count -= 1
                    else:
                        zeroes -= 1
                    beg += 1
                max_length = max(count+zeroes, max_length)
            return max_length
        else:
            return 1
