class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = defaultdict(int)
        for src, end in prerequisites:
            graph[end].append(src)
            inDegree[src] = 1 + inDegree.get(src,0)
        ans = []
        queue = deque()
        visited = set()
        for key in range(numCourses):
            if inDegree[key] == 0:
                queue.append(key)
                visited.add(key)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in graph[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)
                    visited.add(child)
        if len(ans) == numCourses:
            return ans
        return []
                