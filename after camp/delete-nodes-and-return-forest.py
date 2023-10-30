# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.to_delete = set(to_delete)
        self.arr = []
        if root.val not in self.to_delete:
            self.arr=[root]
        self.dfs(root)
        return self.arr
        
    def dfs(self,root):
        if not root:
            return (None,False)
        left,b_left = self.dfs(root.left)
        right,b_right = self.dfs(root.right)
        if b_left:
            root.left = None
        if b_right:
            root.right = None
                    
        if root.val in self.to_delete:
            if left and not b_left:
                self.arr.append(left)
            if right and not b_right:
                self.arr.append(right)
            return(root,True)
        return (root,False)
        