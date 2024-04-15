# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = []
        self.dfs(root,[])
        return sorted(self.ans)[0]
    def dfs(self,node,path):
        if not node.left and not node.right:
            self.ans.append("".join([chr(node.val+97)]+path))
            return
        if node.left:
            self.dfs(node.left, [chr(node.val+97)] + path)
        if node.right:
            self.dfs(node.right, [chr(node.val+97)] + path)
        