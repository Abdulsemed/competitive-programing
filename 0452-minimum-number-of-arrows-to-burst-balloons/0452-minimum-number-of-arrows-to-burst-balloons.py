class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0],x[1]))
        curr= points[0]
        count = 1
        for index in range(len(points)):
            if curr[0] <= points[index][0] <= curr[1]:
                if points[index][1] < curr[1]:
                    curr[1] = points[index][1]
            else:
                count += 1
                curr = points[index]
                
        return count