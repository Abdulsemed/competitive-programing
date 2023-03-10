# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.level= []
        self.size = -1
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root,0)
        return self.level
    def traverse(self,root, depth):
        if root == None:
            return None
        if depth > self.size:
            self.level.append([root.val])
            self.size += 1
        else:
            self.level[depth].append(root.val)
        self.traverse(root.left, depth+1)
        self.traverse(root.right, depth+1)
            
        