class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        prob = {node:0 for node in range(n)}
        prob[start_node] = 1
        
        queue = [(-prob[start_node], start_node)]
        visited = set()
        graph = defaultdict(list)
        
        for index in range(len(edges)):
            graph[edges[index][0]].append((edges[index][1], succProb[index]))
            graph[edges[index][1]].append((edges[index][0], succProb[index]))
            
        while queue:
            curr_prob, node = heapq.heappop(queue)
            if node in visited:
                continue
                
            visited.add(node)
            for child, probability in graph[node]:
                if -curr_prob * probability > prob[child]:
                    prob[child] = -curr_prob * probability
                    heapq.heappush(queue, (-prob[child], child))
            
        return prob[end_node]
            
            