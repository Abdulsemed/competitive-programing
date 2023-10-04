class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float("inf") if index != val else 0 for index in range(numCourses) ]
                for val in range(numCourses)]
        
        for src,end in prerequisites:
            dist[src][end] = 1
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        answer = []
        for src,end in queries:
            if dist[src][end] == float("inf"):
                answer.append(False)
            else:
                answer.append(True)
                
        return answer