class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        size = len(matrix)
        for index in range(size):
            for val in range(size):
                heapq.heappush(heap,matrix[index][val])
                
        for index in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)