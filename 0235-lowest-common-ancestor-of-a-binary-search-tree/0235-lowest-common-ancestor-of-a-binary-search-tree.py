# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        list1 = self.traverse(root,[],p)
        list2 = set(self.traverse(root,[],q))
        for index in range(len(list1)-1,-1,-1):
            if list1[index] in list2:
                return list1[index]
    def traverse(self,root,dict1,target):
        dict1.append(root)
        if root.val == target.val:
            return dict1
        elif root.val < target.val:
            self.traverse(root.right,dict1,target)
        else:
            self.traverse(root.left,dict1, target)
        return dict1
        