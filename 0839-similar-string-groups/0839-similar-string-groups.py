class Solution:
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])
        return self.dicts[node]
    
    def union(self, node1, node2,strs):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return 
        count = 0
        for index in range(len(strs[node1])):
            if strs[node1][index] != strs[node2][index]:
                count += 1
            if count > 2: break
        if count <=2:
            if self.size[rep1] > self.size[rep2]:
                self.dicts[rep2] = rep1
                self.size[rep1] += self.size[rep2]
            else:
                self.dicts[rep1] = rep2
                self.size[rep2] += self.size[rep1]
                        
    def numSimilarGroups(self, strs: List[str]) -> int:
        size = len(strs)
        self.dicts = {}
        self.size = [1] *(size)
        for index in range(size):
            self.dicts[index] = index
        for index in range(size):
            for val in range(index+1, size):
                self.union(index, val,strs) 
        count = 0
        for key in self.dicts:
            if key == self.dicts[key]:
                count += 1
                
        return count
            