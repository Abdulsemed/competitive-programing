class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        dicts = {}
        maxim = 0
        for index in range(len(edges)):
            graph[edges[index][0]].append(edges[index][1])
            graph[edges[index][1]].append(edges[index][0])
            if len(graph[edges[index][0]])  > 1:
                return edges[index][0]
            elif len(graph[edges[index][1]]) > 1:
                return edges[index][1]
            
        