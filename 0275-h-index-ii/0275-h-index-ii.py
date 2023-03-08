class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        size = len(citations)
        right = size-1
        while left <= right:
            mid = left + (right-left)//2
            if citations[mid] <  size - mid:
                left = mid + 1
            else:
                right = mid - 1
        return size - left
            