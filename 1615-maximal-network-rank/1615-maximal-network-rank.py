class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for start, end in roads:
            graph[start].append(end)
            graph[end].append(start)
        answer = 0
        count = 0
        visited = set()
        for key in graph:
            count = 0
            for node in graph[key]:
                subCount = 0
                if node not in visited:
                    for child in graph[node]:
                        if child != key :
                            subCount += 1
                    count = max(count, subCount)
                    
            for vertex in graph:
                if vertex not in graph[key] and key != vertex:
                    count = max(count , len(graph[vertex]))
            answer = max(answer, count+len(graph[key]))
            visited.add(key)
            
        return answer