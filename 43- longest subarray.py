def longestSubarray(self, nums: List[int]) -> int:
        beg =0
        end = 0
        max_size = 0
        pos =[]
        zeroes = 0
        while end < len(nums):
            if nums[end] == 0:
                zeroes += 1
                pos.append(end)
            if zeroes > 1:
                zeroes -= 1
                beg = pos[0] + 1
                pos.pop(0)
            max_size = max(max_size, len(nums[beg:end]))
            end += 1
        return max_size
