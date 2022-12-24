class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = 0
        distance = 0
        leastDistance = float("inf")
        indexes = -1
        for index, point in enumerate(points):
            if x == point[0] or y == point[1]:
                distance = (x-point[0])**2 + (y-point[1])**2
                
                if distance < leastDistance:
                    indexes = index
                    leastDistance = distance
                    
        return indexes
            
        
        