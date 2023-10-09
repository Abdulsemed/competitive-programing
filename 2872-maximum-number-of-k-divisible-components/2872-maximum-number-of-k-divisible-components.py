class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        
        for src, end in edges:
            graph[src].append(end)
            graph[end].append(src)
           
        visited = set()
        def dfs(root):
            if root in visited:
                return (0,0)
            visited.add(root)
            curr = [values[root],0]
            
            for child in graph[root]:
                val, count = dfs(child)
                curr[0] += val
                curr[1] += count
                
            if curr[0] % k == 0:
                curr[0] = 0
                curr[1] += 1
                
                
            return curr
        count  = 0
        for index in range(n):
            count += dfs(index)[1]
        return count