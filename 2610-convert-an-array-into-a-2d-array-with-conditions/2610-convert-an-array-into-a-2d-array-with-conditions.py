class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        graph = defaultdict(set)
        while nums:
            val = nums.pop()
            flag = False
            for index in range(len(graph)):
                if val not in graph[index]:
                    graph[index].add(val)
                    flag = True
                    break
            if not flag:
                graph[len(graph)].add(val)
        ans = []
        for key in graph:
            ans.append(graph[key])
        return ans