class Solution:
    def __init__(self):
        self.dicts = {}
    def find(self,node):
        if node != self.dicts[node][0]:
            self.dicts[node][0] = self.find(self.dicts[node][0])[0]
        return self.dicts[node]
    def union(self,node1,node2):
        rep_1 = self.find(node1)
        rep_2 = self.find(node2)
        if rep_1  == rep_2:
            return
        elif rep_1[1] > rep_2[1]:
            self.dicts[rep_2[0]][0] = rep_1[0]
            self.dicts[rep_1[0]][1] += rep_2[1]+1
        else:
            self.dicts[rep_1[0]][0] = rep_2[0]
            self.dicts[rep_2[0]][1] += rep_1[1] +1
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.dicts ={i:[i,0] for i in range(n)}
        for src,end in edges:
            self.union(src,end)
        return self.find(destination)[0] == self.find(source)[0]