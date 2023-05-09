class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0]*(numCourses)
        for src, end in prerequisites:
            graph[end].append(src)
            inDegree[src] += 1 
        ans = []
        queue = deque()
        for key in range(numCourses):
            if inDegree[key] == 0:
                queue.append(key)
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for child in graph[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)
        if len(ans) == numCourses:
            return ans
        return []
                