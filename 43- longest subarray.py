def longestSubarray(self, nums: List[int]) -> int:
        count =0
        max_size = 0
        beg = 0
        zeroes = -1
        for i, elt in enumerate(nums):
            if elt == 1:
                count += 1
            elif elt == 0 and zeroes == -1:
                zeroes = i
            elif elt == 0:
                count -= len(nums[beg:zeroes])
                beg = zeroes +1
                zeroes = i
            if zeroes == -1:
                max_size = max(max_size, count-1)
            else:
                max_size = max(max_size, count)
        return max_size    
