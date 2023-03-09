# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        list1 = tuple(self.traverse(root,[],p))
        list2 = tuple(self.traverse(root,[],q))
        for element in list1:
            if element in list2:
                val = element
        return val
    def traverse(self,root,dict1,target):
        dict1.append(root)
        if root.val == target.val:
            return dict1
        elif root.val < target.val:
            self.traverse(root.right,dict1,target)
        else:
            self.traverse(root.left,dict1, target)
        return dict1
        