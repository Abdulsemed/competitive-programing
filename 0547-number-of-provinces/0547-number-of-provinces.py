class Solution:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = set()
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        for index in range(size):
            for val in range(size):
                if isConnected[index][val] == 1:
                    self.graph[index].append(val)
        count = 0
        for key in self.graph:
            if key not in self.visited:
                self.dfs(key)
                count += 1
                
        return count
    def dfs(self, node):
        self.visited.add(node)
        
        if node in self.graph:
            for child in self.graph[node]:
                if child not in self.visited:
                    self.dfs(child)
        