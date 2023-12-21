class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0],x[1]))
        count = 0
        for index in range(1,len(points)):
            count = max(count, points[index][0] - points[index-1][0])
            
        return count