class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        size = len(nums)
        prefixSum = [ 0 for index in range(size+1)]
        for req in requests:
            prefixSum[req[0]] += 1
            prefixSum[req[1]+1] -= 1
            
        for index in range(1,size+1):
            prefixSum[index] += prefixSum[index-1]
        prefixSum.sort(reverse = True)
        
        val = 0
        for index in range(size):
            val += (nums[index]*prefixSum[index])
        return val%(1000000007)