class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        heap = []
        for index in range(len(nums)):
            while heap and heap[0][0]+1 < nums[index]:
                if heapq.heappop(heap)[1] < 3:
                    return False
            if not heap or heap[0][0] == nums[index]:
                heapq.heappush(heap,[nums[index],1])
            else:
                arr = heapq.heappop(heap)
                arr[0]= nums[index]
                arr[1] += 1
                heapq.heappush(heap,arr)
        while heap:
            if heapq.heappop(heap)[1] < 3:
                return False
        return True
                