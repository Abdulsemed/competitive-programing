class Solution:
    def __init__(self):
        self.dicts = {}
        self.size = []
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    
    def union(self,node1,node2):
        rep_1 = self.find(node1)
        rep_2 = self.find(node2)
        if rep_1 == rep_2:
            return True
        elif self.size[rep_1] > self.size[rep_2]:
            self.dicts[rep_2] = rep_1
            self.size[rep_1] += self.size[rep_2]
        else:
            self.dicts[rep_1] = rep_2
            self.size[rep_2] += self.size[rep_1]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        self.dicts = {index:index for index in range(len(edges))}
        self.size = [1]*(len(edges))
        for src,end in edges:
            if self.union(src-1,end-1):
                ans.append([src,end])
        return ans[-1]