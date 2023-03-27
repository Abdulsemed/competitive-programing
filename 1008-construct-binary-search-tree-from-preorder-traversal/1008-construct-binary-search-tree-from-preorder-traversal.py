# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     get idea for the parent
    def __init__(self):
        self.visited = []
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        self.visited = [[preorder[0],root]]
        self.traverse(1, preorder, root)
        return root
    def traverse(self, idx, preorder, root):
        for index in range(idx, len(preorder)):
            val = TreeNode(preorder[index])
            flag =False
            while self.visited and self.visited[-1][0] <preorder[index]:
                flag = True
                last = self.visited.pop()[1]
            if flag:
                last.right = val
            else:
                self.visited[-1][1].left = val
            self.visited.append([preorder[index], val])
            
            
        