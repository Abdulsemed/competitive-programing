def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        current_sum = 0
        p_sum = {0: 1}
        counter = 0
        for elt in nums:
            current_sum += elt
            diff = current_sum - k
            counter += p_sum.get(diff, 0)
            p_sum[current_sum] = 1 + p_sum.get(current_sum, 0)

        return counter
