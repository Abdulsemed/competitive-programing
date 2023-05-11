class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for src,end in edges:
            graph[src].append(end)
            degree[end] += 1
        ans = [set() for index in range(n)]
        queue = deque()
        for index in range(n):
            if degree[index] == 0:
                queue.append(index)
        while queue:
            curr = queue.popleft()
            for child in graph[curr]:
                ans[child].add(curr)
                for val in ans[curr]:
                    ans[child].add(val)
                degree[child] -= 1
                if degree[child] == 0:
                    queue.append(child)
        for index in range(n):
            if ans[index]:
                ans[index] = sorted(list(ans[index]))
        return ans