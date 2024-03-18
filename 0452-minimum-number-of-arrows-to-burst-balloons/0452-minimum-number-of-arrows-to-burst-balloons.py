class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[1]))
        curr= points[0][1]
        count = 1
        for index in range(len(points)):
            if points[index][0] > curr:
                count += 1
                curr = points[index][1]
                
        return count