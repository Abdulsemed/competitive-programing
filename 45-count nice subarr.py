def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i,elt in enumerate(nums):
            if elt % 2 != 0:
                nums[i] = 1
            else:
                nums[i] = 0
        hash_map = {0: 1}
        p_sum = 0
        count = 0
        for i, elt in enumerate(nums):
            p_sum += nums[i]
            if p_sum - k in hash_map:
                count += hash_map[p_sum - k]
            hash_map[p_sum] = 1 + hash_map.get(p_sum, 0)
            
        return count
