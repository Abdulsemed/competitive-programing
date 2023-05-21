class Solution:
    def __init__(self):
        self.reps = {}
        self.size = []
    def find(self,node):
        if node != self.reps[node]:
            self.reps[node] = self.find(self.reps[node])
        return self.reps[node]
    
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return True
        elif self.size[rep1] > self.size[rep2]:
            self.reps[rep2] = rep1
            self.size[rep1] += self.size[rep2]
        else:
            self.reps[rep1] = rep2
            self.size[rep2] += self.size[rep1]  
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.size = [1]*(len(points))
        ans = []
        for index in range(len(points)):
            self.reps[index] = index
            for val in range(index+1, len(points)):
                manhat = abs(points[index][0]- points[val][0])+ abs(points[index][1] - points[val][1])
                ans.append([manhat,(index,val)])
        ans.sort()
        path = 0
        for size,dirc in ans:
            if not self.union(dirc[0],dirc[1]):
                path += size
        return path
        