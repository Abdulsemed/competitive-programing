class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*(n)
        for index in range(n):
            if leftChild[index] != -1:
                graph[index].append(leftChild[index])
                indegree[leftChild[index]] += 1
            if rightChild[index] != -1:
                graph[index].append(rightChild[index])
                indegree[rightChild[index]] += 1
            
        visited = set()
        stack =[]
        for child in range(n):
            if not stack and indegree[child] == 0:
                stack.append(child)
            if indegree[child] > 1:
                return False
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for child in graph[curr]:
                stack.append(child)
        if len(visited) == n:
            return True
        return False