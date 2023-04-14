# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            path = self.dfs(root,[])
            return ''.join(path[1:-1])
        return []
    def dfs(self,root,path):
        if not root:
            return path
        path.append("(")
        path.append(str(root.val))
        if not root.left and  root.right:
            path.append("()")
        path = self.dfs(root.left,path)
        path = self.dfs(root.right, path)
        
            
        path.append(")")
        return path