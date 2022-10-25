def longestSubarray(self, nums: List[int]) -> int:
        beg =0
        end = 0
        max_size = 0
        pos =-1
        count = 0
        while end < len(nums):
            if nums[end] == 0 and pos == -1:
                pos = end
            elif nums[end]==0  :
                count -= len(nums[beg:pos])
                beg = pos + 1
                pos = end
            else:
                count += 1
            if pos == -1:
                max_size = max(max_size, count-1)
            else:
                max_size = max(max_size, count)
            end += 1
        return max_size
