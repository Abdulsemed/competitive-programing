class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = heapq.nlargest(k,nums)
        return ans[k-1]