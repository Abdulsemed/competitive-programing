class Solution:
    def find(self,node):
        if node != self.dicts[node]:
            self.dicts[node] = self.find(self.dicts[node])    
        return self.dicts[node]
    
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        
        if rep1 == rep2:
            return 
        if rep1 in self.sets:
            self.dicts[rep2] = rep1
        else:
            self.dicts[rep1] = rep2
    
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        self.dicts = {node:node for node in range(n)}
        meetings.sort(key = lambda x:(x[2]))
        self.sets = {firstPerson, 0}
        graph = defaultdict(list)
        for a,b,time in meetings:
            graph[time].append([a,b])
            
        for key in graph:
            flag = False
            for src, end in graph[key]:
                self.union(src,end)
    
            for src, end in graph[key]:
                if self.find(src) not in self.sets:
                    self.dicts[src] = src
                if self.find(end) not in self.sets:
                    self.dicts[end] = end
                    
        for index in range(n):
            if self.find(index) in self.sets:
                self.sets.add(index)
                
        return list(self.sets)
        
        