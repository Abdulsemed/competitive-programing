class Solution:
    def __init__(self):
        self.dicts = {}
        self.size ={} 
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2  = self.find(node2)
        if rep1 == rep2:
            return 
        elif self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.dicts[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.dicts[rep1] = rep2
    def removeStones(self, stones: List[List[int]]) -> int:
        for index in range(len(stones)):
            self.dicts[index] = index
            self.size[index] = 1
        for index in range(len(stones)):
            for val in range(index,len(stones)):
                if stones[index][0] == stones[val][0] or stones[index][1] == stones[val][1]:
                    self.union(index,val)
        ans = 0
        for key in self.dicts:
            if key == self.dicts[key]:
                ans += self.size[key]-1
        return ans
        
        