class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for index in range(len(piles)):
            piles[index] *= -1
        heapq.heapify(piles)
        for _ in range(k):
            val = heapq.heappop(piles)//2
            heapq.heappush(piles,val)
        for index in range(len(piles)):
            if piles[index]:
                piles[index] *= -1
        return sum(piles)