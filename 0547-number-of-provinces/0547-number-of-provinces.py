class Solution:
    def __init__(self):
        self.dicts = {}
        self.size = []
        
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return
        elif self.size[rep1] > self.size[rep2]:
            self.size[rep1] += self.size[rep2]
            self.dicts[rep2] = rep1
        else:
            self.size[rep2] += self.size[rep1]
            self.dicts[rep1] = rep2
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        self.size =[1]*(length)
        for index in range(length):
            self.dicts[index] = index
        for index in range(length):
            for idx in range(len(isConnected[index])):
                if isConnected[index][idx] != 0:
                    self.union(index,idx)
        provinces = 0
        for key in self.dicts:
            if key == self.dicts[key]:
                provinces += 1
                
        return provinces
            