class Solution:
    def __init__(self):
        self.dicts = {}
    def find(self,node):
        if node == self.dicts[node][0]:
            return self.dicts[node]
        rep = self.find(self.dicts[node][0])
        self.dicts[node][0] = rep[0]
        return rep
    
    def union(self,node1,node2):
        rep_1 = self.find(node1)
        rep_2 = self.find(node2)
        if rep_1 == rep_2:
            return True
        elif rep_1[1] > rep_2[1]:
            self.dicts[rep_2[0]][0] = rep_1[0]
            self.dicts[rep_1[0]][1] += rep_2[1]
        else:
            self.dicts[rep_1[0]][0] = rep_2[0]
            self.dicts[rep_2[0]][1] += rep_1[1]

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ans = []
        self.dicts = {index:[index,1] for index in range(len(edges))}
        for src,end in edges:
            if self.union(src-1,end-1):
                ans.append([src,end])
        return ans[-1]