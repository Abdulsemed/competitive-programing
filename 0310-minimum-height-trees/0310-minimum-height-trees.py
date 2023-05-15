class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n== 1: return [0]
        graph = defaultdict(list)
        for src, end in edges:
            graph[src].append(end)
            graph[end].append(src)
        ans = []    
        sets = set()
        queue = deque()
        for key in graph:
            if len(graph[key]) == 1:
                queue.append(key)
                sets = set()
        counts = [0]*(n)
        while queue:
            length = len(queue)
            ans = queue.copy()
            for _ in range(length):
                curr = queue.popleft()
                for child in graph[curr]:
                    counts[child] += 1
                    if counts[child]+1 == len(graph[child]) and child not in sets:
                        queue.append(child)
                        sets.add(child)
        return ans