class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        duplicate = set()
        graph = defaultdict(list)
        for child in leftChild:
            if child != -1:
                if child in duplicate:
                    return False
                duplicate.add(child)

        for child in rightChild:
            if child != -1:
                if child in duplicate:
                    return False
                duplicate.add(child)



        for i in range(n):
            # self loop check
            if i == leftChild[i] or i == rightChild[i]:
                return False
            if leftChild[i] != -1:
                graph[i].append(leftChild[i])
            if rightChild[i] != -1:
                graph[i].append(rightChild[i])

        root = []

        for i in range(n):
            if i not in duplicate:
                root.append(i)

        #only one root is assured
        if len(root) != 1:
            return False
        stack = [root[0]]
        visited = {root[0]}
        while stack:
            curr = stack.pop()
            for child in graph[curr]:
                if child in visited:
                    return False
                stack.append(child)
                visited.add(child)
                
        return len(visited) == n