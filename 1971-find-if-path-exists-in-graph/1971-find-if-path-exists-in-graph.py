class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for index in range(len(edges)):
            graph[edges[index][0]].append(edges[index][1])
            graph[edges[index][1]].append(edges[index][0])
        stack = [source]
        visited = set()
        while stack:
            currNode = stack.pop()
            if currNode == destination:
                return True
            visited.add(currNode)
            for adj_node in graph[currNode]:
                if adj_node not in visited:
                    stack.append(adj_node)
                    
        return False