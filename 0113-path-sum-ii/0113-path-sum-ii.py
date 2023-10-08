# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.dfs(root,[],targetSum)
        return self.ans
        
    def dfs(self,root,path,targetSum):
        if root == None:
            return
        
        path.append(root.val)
        self.dfs(root.left, path, targetSum)
        self.dfs(root.right, path, targetSum)
        if not root.left and not root.right:
             if sum(path) == targetSum:
                self.ans.append(path[:])
        path.pop()
        