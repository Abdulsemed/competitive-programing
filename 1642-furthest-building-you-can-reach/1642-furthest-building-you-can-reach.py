class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        weightCount = 0
        ladderCount = 0
        index = 0
        for index in range(1,len(heights)):
            value = heights[index] - heights[index-1]
            if value > 0:
                if ladderCount < ladders:
                    heapq.heappush(heap,value)
                    ladderCount += 1
                    continue
                heapq.heappush(heap,value)
                weight = heapq.heappop(heap)
                if weight + weightCount <= bricks:
                    weightCount += weight
                else:
                    return index-1
        return index