class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set()
        visited = set()
        for start, end in edges:
            if start not in visited:
                ans.add(start)
            if end in ans:
                ans.remove(end)
            visited.add(start)
            visited.add(end)
        return list(ans)
                
            