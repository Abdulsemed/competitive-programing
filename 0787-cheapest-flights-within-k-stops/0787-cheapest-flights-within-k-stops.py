class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph  = defaultdict(list)
        dist = {node: [float("inf"), k+1] for node in range(n)}
        
        for a,b,length in flights:
            graph[a].append((b, length))
        
        dist[src] = [0,0]
        queue = [(0,0,src)]
        visited = defaultdict(int)
        while queue:
            curr_dist,stops, node = heapq.heappop(queue)
            
            if visited[(node,stops)] != 0 and visited[(node,stops)] < curr_dist:
                continue
            visited[(node,stops)] = curr_dist
            
            for child, leng in graph[node]:
                if stops <= k:
                    if curr_dist + leng < dist[child][0] or (child != dst and stops + 1 <= dist[child][1]):
                        dist[child] = [curr_dist+leng, stops+1]
                        heapq.heappush(queue, (curr_dist + leng, stops+1, child))
                
        
        if dist[dst][0] != float("inf"):
            return dist[dst][0]
        return -1