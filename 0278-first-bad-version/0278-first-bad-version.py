# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n-1
        while n:
            mid = left + (right-left)//2
            if not isBadVersion(mid+1):
                left = mid+1
            elif not isBadVersion(mid):
                return mid+1
            else:
                right = mid -1