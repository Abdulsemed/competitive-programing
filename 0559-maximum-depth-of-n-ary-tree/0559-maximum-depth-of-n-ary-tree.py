"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.count = 0
    def maxDepth(self, root: 'Node') -> int:
        if root:
            self.dfs(root, 1)
        
        return self.count
    def dfs(self, node, depth):
        if not node.children:
            self.count = max(self.count, depth)
        
        for child in node.children:
            self.dfs(child, depth+1)
            