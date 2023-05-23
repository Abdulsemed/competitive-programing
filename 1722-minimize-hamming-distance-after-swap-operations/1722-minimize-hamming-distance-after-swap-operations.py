class Solution:
    def __init__(self):
        self.reps = {}
        self.dicts = defaultdict(dict)
    def find(self, node):
        if node != self.reps[node]:
            self.reps[node] = self.find(self.reps[node])
        return self.reps[node]
    def union(self,node1, node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return 
        if len(self.dicts[rep1]) > len(self.dicts[rep2]):
            self.reps[rep2] = rep1
            for element in self.dicts[rep2]:
                self.dicts[rep1][element] = self.dicts[rep2][element] + self.dicts[rep1].get(element,0)
            
        else:
            self.reps[rep1] = rep2
            for element in self.dicts[rep1]:
                self.dicts[rep2][element] = self.dicts[rep1][element]+ self.dicts[rep2].get(element,0)
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        for index in range(len(source)):
            self.reps[index] = index
            self.dicts[index][source[index]] = 1 + self.dicts[index].get(source[index],0)
        for src, end in allowedSwaps:
            self.union(src, end)
        count = 0
        for index in range(len(source)):
            rep = self.find(index)
            if target[index] in self.dicts[rep] and self.dicts[rep][target[index]] > 0:
                self.dicts[rep][target[index]] -= 1
            else:
                count += 1
        return count
            
        