# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val,root,None)
        def dfs(node,dep):
            if not node:
                return
            if dep == depth:
                leftCurr = TreeNode(val,node.left,None)
                rightCurr = TreeNode(val,None,node.right)
                node.left = leftCurr
                node.right = rightCurr
                return
            dfs(node.left,dep+1)
            dfs(node.right, dep+1)
            
        dfs(root,2)
        return root
        