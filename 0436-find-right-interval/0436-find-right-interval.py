class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        size = len(intervals)
        rightIntervals = [-1]*size
        intervals = [(intervals[i], i) for i in range(size)]
        intervals.sort()
        for interval in intervals:
            left = 0
            right = size-1
            while left<= right:
                mid = left + (right-left)//2
                if intervals[mid][0][0] < interval[0][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if left < size:
                rightIntervals[interval[1]] = intervals[left][1]
        return rightIntervals