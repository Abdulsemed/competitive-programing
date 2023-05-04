class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        heapq.heapify(self.nums)
        for index in range(len(nums)-k):
            heapq.heappop(self.nums)
        self.k = k
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
            
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)