# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lists = []
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.traverse(root,[])
        return self.lists
    def traverse(self,root,path):
        if root == None:
            return 
        else:
            path.append(str(root.val))
            self.traverse(root.left,path)
            self.traverse(root.right, path)
            if not root.left and  not root.right:
                self.lists.append('->'.join(path))
                path.pop()
            else:
                path.pop()