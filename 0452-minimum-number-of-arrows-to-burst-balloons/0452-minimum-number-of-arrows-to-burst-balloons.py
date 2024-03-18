class Solution:
    def find(self,node):
        if self.dicts[node] != node:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    
    def union(self, node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        size1 = self.size[rep1]
        size2 = self.size[rep2]
        if rep1 == rep2:
            return 
        elif size1[0] <= size2[0] <= size1[1]:
            self.size[rep1] =(size1[0], min(size2[1],size1[1]))
            self.dicts[rep2] = rep1 
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        self.dicts = {}
        self.size = {}
        points.sort(key = lambda x:(x[0],x[1]))
        for index in range(len(points)):
            points[index] = tuple(points[index])
            self.dicts[points[index]] = points[index]
            self.size[points[index]] = points[index]
            
        for index in range(len(points)-1):
            self.union(points[index], points[index+1])
        
        count = 0
        visited = set()
        for point in points:
            if self.find(point) == point and point not in visited:
                count += 1
            visited.add(point)
        return count