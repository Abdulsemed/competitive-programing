class Solution:
    def __init__(self):
        self.count = 0
        self.visited = {0}
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for src,end in edges:
            graph[src].append(end)
            graph[end].append(src)
        self.dfs(0,graph,hasApple)
        return self.count
        
    def dfs(self,root,graph,hasApple):
        
        flag= False
        self.visited.add(root)
        for child in range(len(graph[root])):
            if graph[root][child] in self.visited: continue
            self.visited.add(graph[root][child])
            if self.dfs(graph[root][child],graph,hasApple):
                self.count += 2
                flag = True
        
        return (flag or hasApple[root])
        
                
        