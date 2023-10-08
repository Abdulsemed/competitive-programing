class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for index in range(len(equations)):
            graph[equations[index][0]].append([equations[index][1], values[index]])
            graph[equations[index][1]].append([equations[index][0], 1/values[index]])
            
        answer = []
        for src, end in queries:
            if src in graph and src == end:
                answer.append(1)
            elif src in graph and end in graph:
                dist = {node : float("inf") for node in graph}
                queue = [(1,src)]
                visited = set()
                while queue:
                    curr_val, node = heapq.heappop(queue)
                    
                    if node in visited:
                        continue
                        
                    visited.add(node)
                    for child, val in graph[node]:
                        if curr_val * val < dist[child]:
                            dist[child] = curr_val * val
                            heapq.heappush(queue, [dist[child], child])
                            
                if dist[end] != float("inf"):
                    answer.append(dist[end])
                else:
                    answer.append(-1)               
            else:
                answer.append(-1)
        return answer           