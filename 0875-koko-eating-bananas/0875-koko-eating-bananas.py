class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left<= right:
            mid = left + (right-left)//2
            count =0
            for element in piles:
                count += math.ceil(element/mid)
            if count <= h:
                right = mid -1
            elif count > h:
                left = mid + 1
        return left