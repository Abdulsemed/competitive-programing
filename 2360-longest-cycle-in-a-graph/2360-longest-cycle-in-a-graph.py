class Solution:
    def __init__(self):
        self.visited = set()
        self.val = -1
        self.count = -1
    def cycle(self,node,graph,colors):
        if colors[node] == 2:
            return True
        if colors[node] == 1:
            if self.val == -1 and node not in self.visited:
                self.val = node
                self.count = 0
            return False
        colors[node] = 1
        for child in graph[node]:
            if not self.cycle(child,graph,colors):
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
        for index in range(len(edges)):
            if edges[index] != -1:
                graph[index].append(edges[index])
        count = -1
        for index in range(size):
            self.count = -1
            self.val = -1
            if index not in self.visited:
                self.cycle(index,graph,colors)
            self.visited.add(index)
            count = max(self.count,count)
        return count