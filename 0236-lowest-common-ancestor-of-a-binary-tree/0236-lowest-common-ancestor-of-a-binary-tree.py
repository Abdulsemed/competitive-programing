# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        list1 = self.traverse(root,[],p)
        list2 = self.traverse(root,[],q)
        for element in list1:
            if element in list2:
                val = element
        return val
    def traverse(self,root,lists,target):
        if root == None:
            return lists
        elif root.val == target.val:
            lists.append(root)
            return lists
        elif lists and lists[-1].val == target.val:
            return lists
        else:
            lists.append(root)
            self.traverse(root.left,lists,target)
            self.traverse(root.right,lists,target)
            if lists and lists[-1].val != target.val: lists.pop()
            return lists
        