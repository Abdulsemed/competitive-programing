class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1: return adjacentPairs[0]
        graph = defaultdict(list)
        for end,src in adjacentPairs:
            graph[src].append(end)
            graph[end].append(src)
        visited = set()
        stack =deque()
        for key in graph:
            if len(graph[key]) == 1:
                stack.append(key)
                break
        ans = []
        while stack:
            curr = stack.popleft()
            ans.append(curr)
            for child in graph[curr]:
                if (curr,child) not in visited and (child,curr) not in visited:
                    visited.add((curr,child))
                    stack.append(child)
        return ans