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
            
        
        stack =[]
        for child in range(n):
            if indegree[child] == 0:
                stack.append(child)
                break
        visited = set() if not stack else {stack[0]}
        while stack:
            curr = stack.pop()
            for child in graph[curr]:
                if child in visited:
                    return False
                stack.append(child)
                visited.add(child)
                
        return len(visited) == n