class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for index in range(len(stones)):
            stones[index] *= -1
        heapq.heapify(stones)
        while len(stones)>1:
            val1 = abs(heapq.heappop(stones))
            val2 = abs(heapq.heappop(stones))
            if val1 != val2:
                heapq.heappush(stones,val2-val1)
        if stones:
            return stones[0]*-1
        return 0
            