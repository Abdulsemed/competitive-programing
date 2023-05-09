class Solution:
    def topSort(self,node,graph,colors,ans):
        if colors[node] == 1:
            return False
        if colors[node] == 2:
            return True
        colors[node] = 1
        for child in graph[node]:
            if not self.topSort(child,graph,colors,ans):
                return False
        colors[node] = 2
        ans.append(node)
        return True
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        size = len(graph)
        graphs = defaultdict(list)
        colors = [0]*(size)
        ans = []       
        for key in range(size):
            self.topSort(key,graph,colors,ans)  
        ans.sort()    
        return ans
                