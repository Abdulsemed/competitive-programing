class Solution:
    def __init__(self):
        self.lists = []
        self.graph = defaultdict(list)
        self.visited = set()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        size = len(graph)
        for index in range(size):
            self.graph[index] = graph[index]
            
        self.dfs(0,[0],size-1)
        return self.lists
    def dfs(self,node,path,size):
        self.visited.add(node)
        if node == size:
            self.lists.append(path[:])
            return 
        for child in self.graph[node]:
                path.append(child)
                self.dfs(child,path[:],size)
                path.pop()
                
            