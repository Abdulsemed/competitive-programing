class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1]*(n)
        graph = defaultdict(list)
        for start,end in redEdges:
            graph[start].append([end,1])
        
        for start, end in blueEdges:
            graph[start].append([end,0])

        queue = deque([[0,-1,0]])
        visited = {(0,-1)}
        while queue:
            node,color, count = queue.popleft()
            if ans[node] == -1:
                ans[node] = count
            else:
                ans[node] = min(ans[node], count)
            for child,clr in graph[node]:
                if clr != color:
                    if (child,clr) not in visited:
                        visited.add((child,clr))
                        queue.append([child,clr,count+1])
            
        return ans

