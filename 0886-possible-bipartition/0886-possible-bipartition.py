class Solution:
    def __init__(self):
        self.arr = []
        self.visited = set()
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.arr = [0]*n
        size = len(dislikes)
        graph = defaultdict(list)
        for src, end in dislikes:
            graph[src].append(end)
            graph[end].append(src)
        for key in graph:
            if key not in self.visited:
                color1 = 1
                color2 = 2
                if self.arr[key-1] == 1:
                    color1, color2 = color2, color1
                bools = self.dfs(key,graph,color1, color2)
                if not bools:
                    return False
        return True       
    def dfs(self,node,graph,color1, color2):
        self.visited.add(node)
        self.arr[node-1] = color2
        if node in graph:
            for child in graph[node]:
                if child not in self.visited:
                    self.arr[child-1] = color1
                    bools = self.dfs(child,graph,color2,color1)
                    if not bools:
                        return False
                elif self.arr[node-1] == self.arr[child-1]:
                    return False
        return True
                