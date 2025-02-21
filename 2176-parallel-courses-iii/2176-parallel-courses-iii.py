class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0]*(n)
        currMax = [0]*(n)
        graph = defaultdict(list)
        for src, end in relations:
            graph[src-1].append(end-1)
            indegree[end-1] += 1
        
        queue = deque([])
        for element in range(n):
            if indegree[element] == 0:
                queue.append([element,time[element]])
        ans = 0
        while queue:
            ele,months = queue.popleft()
            ans = max(ans,months)
            for element in graph[ele]:
                indegree[element] -= 1
                currMax[element] = max(currMax[element], months)
                if indegree[element] == 0:
                    queue.append([element,currMax[element]+time[element]])     
                  
        return ans