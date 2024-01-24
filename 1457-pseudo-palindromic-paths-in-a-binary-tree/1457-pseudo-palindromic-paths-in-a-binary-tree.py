# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.dfs(root,{})
        return self.count
    def dfs(self,root,dicts):
        if not root:
            return
        
        dicts[root.val] = 1 + dicts.get(root.val,0)
        self.dfs(root.left,dicts)
        self.dfs(root.right,dicts)
        if not root.left and not root.right:
            odd = 0
            for key in dicts:
                if dicts[key] % 2:
                    odd += 1
                if odd > 1:
                    break
            if odd < 2:
                self.count += 1
        dicts[root.val] -= 1     
        