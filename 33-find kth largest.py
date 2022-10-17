def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        nums = [int(elt) for elt in nums]
        heapq.heapify(nums)
        min_heap = []
        for index in range(len(nums)):
            min_heap.append(str(heapq.heappop(nums)))
        return min_heap[len(min_heap)-k]
