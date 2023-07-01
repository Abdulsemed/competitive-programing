class Solution:
#     let's start with leaf nodes
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = {-1}
        self.maxim = 0
    def longestPath(self, parent: List[int], s: str) -> int:
        size = len(parent)
        for index in range(size):
            self.graph[parent[index]].append(index)
            self.graph[index].append(parent[index])
            
        for index in range(size):
            if index not in self.visited:
                self.dfs(index, s)
        return self.maxim+1
    def dfs(self,idx,s):
        self.visited.add(idx)
        levelMax = []
        ans = 0
        for child in self.graph[idx]:
            if child not in self.visited and s[child] != s[idx]:
                heapq.heappush(levelMax,-self.dfs(child ,s))
            
        val1, val2 = 0, 0
        if levelMax: val1 = heapq.heappop(levelMax)
        if levelMax: val2 = heapq.heappop(levelMax)
        self.maxim = max(self.maxim, -(val1+val2))
        return -val1+1
        
        
       