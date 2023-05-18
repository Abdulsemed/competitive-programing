class Solution:
    def __init__(self):
        self.dicts  = {}
        self.size = {}
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def union(self,node1,node2,size):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if self.size[rep1] == self.size[rep2] == size:
            return
        elif rep1 < rep2:
            self.dicts[rep2] = rep1
            self.size[rep1] = min(self.size[rep1],self.size[rep2],size)
        else:
            self.dicts[rep1] = rep2
            self.size[rep2] = min(self.size[rep1],self.size[rep2],size)
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        for index in range(n):
            self.dicts[index] = index
            self.size[index] = float("inf")
        for src,end,size in roads:
            self.union(src-1,end-1,size)
        return self.size[0]
            
        