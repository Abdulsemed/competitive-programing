# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.dicts = defaultdict(int)
        self.ans = []
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return "" 
        rep = str(root.val) + " "+ self.dfs(root.left) + " " + self.dfs(root.right)
        if self.dicts[rep] == 1:
            self.ans.append(root)
            
        self.dicts[rep] += 1
            
        return rep
            
        
        
        
            