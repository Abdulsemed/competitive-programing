class Solution:
    def __init__(self):
        self.sets = set()
        self.graph = defaultdict(list)
    def dfs(self, node,dest):
        if node == dest:
            return True
        
        self.sets.add(node)
        for adj_node in self.graph[node]:
            if adj_node not in self.sets:
                flag = self.dfs(adj_node, dest)
                if flag:
                    return True
                
        return False
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        for index in range(len(edges)):
            self.graph[edges[index][0]].append(edges[index][1])
            self.graph[edges[index][1]].append(edges[index][0])
            
        return self.dfs(source,destination)