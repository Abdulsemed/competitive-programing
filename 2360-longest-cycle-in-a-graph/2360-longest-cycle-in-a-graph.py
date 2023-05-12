class Solution:
    def __init__(self):
        self.visited = set()
        self.val = -1
        self.count = -1
    def cycle(self,node,edges,colors):
        if colors[node] == 2:
            return True
        if colors[node] == 1:
            if self.val == -1 and node not in self.visited:
                self.val = node
                self.count = 0
            return False
        colors[node] = 1
        if edges[node] != -1:
            if not self.cycle(edges[node],edges,colors):
                if self.val != -1:
                    self.count += 1
                if self.val == node:
                    self.val = -1
                return False
        colors[node] = 2
        return True        
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        size = len(edges)
        colors = [0]*(size)
        count = -1
        for index in range(size):
            self.count = -1
            self.val = -1
            if index not in self.visited:
                self.cycle(index,edges,colors)
            self.visited.add(index)
            count = max(self.count,count)
        return count