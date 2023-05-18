class Solution:
    def __init__(self):
        self.dicts = { chr(i): chr(i) for i in range(97,123)}
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return 
        elif rep1 < rep2:
            self.dicts[rep2] = rep1
        else:
            self.dicts[rep1] = rep2
    def equationsPossible(self, equations: List[str]) -> bool:
        notEquals = []
        for element in equations:
            val1 = element.split("==")
            val2 = element.split("!=")
            if len(val1) == 2:
                self.union(val1[0],val1[1])
            else:
                notEquals.append(val2)
        
        for src, end in notEquals:
            if self.find(src) == self.find(end):
                return False
        return True
            
                
                