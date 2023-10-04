class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {val:float("inf") for val in range(n)}
        dist[k-1] = 0
        graph = defaultdict(list)
        visited = set()
        
        for src,end,weight in times:
            graph[src-1].append([end-1,weight])
             
        queue = [(0,k-1)]
        
        while queue:
            curr_dist, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            
            for child,weight in graph[node]:
                if curr_dist + weight < dist[child]:
                    dist[child] = curr_dist + weight
                    heapq.heappush(queue,(dist[child],child))
                    
        ans = max(dist.values())
        if ans == float("inf"):
            return -1
        return ans
                    