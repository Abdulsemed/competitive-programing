# Definition for a binary tree node.
from collections import deque
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.dfs(root,graph)
        ans = []
        if k == 0:
            return [target.val]
        for key in graph[target]:
            level = 1
            stack = [[key,level]]
            visited = {key,target}
            while stack:
                curr, level = stack.pop()
                if level == k:
                    ans.append(curr.val)
                else:
                    for child in graph[curr]:
                        if child not in visited:
                            stack.append([child,level+1])
                            visited.add(child)
        return ans
    def dfs(self,root,graph):
        if not root:
            return
        self.dfs(root.left,graph)
        self.dfs(root.right,graph)
        if root and root.left:
            graph[root.left].append(root)
            graph[root].append(root.left)
        if root and root.right:
            graph[root.right].append(root)
            graph[root].append(root.right)
        
        
        