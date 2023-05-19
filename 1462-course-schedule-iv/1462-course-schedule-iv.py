class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dicts = defaultdict(set)
        inDegree = [0]*(numCourses)
        for src,end in prerequisites:
            dicts[src].add(end)
            inDegree[end] += 1
        queue = deque()
        for index in range(numCourses):
            if inDegree[index] == 0:
                queue.append(index)
        holder = dicts.copy()       
        while queue:
            curr = queue.popleft()
            for child in dicts[curr]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    queue.append(child)
            for key in dicts:
                if curr in holder[key]:
                    holder[key] = holder[key].union(holder[curr])
        ans = []
        for src,end in queries:
            if end in holder[src]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
                    
                