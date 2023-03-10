# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.path = []
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.count
    def traverse(self,root):
        if root == None:
            return None
        self.path.append([root.val,0])
        self.traverse(root.left)
        self.traverse(root.right)
        if not root.left and not root.right:
            self.count += 1
            self.path[-1][1] += 1
        elif (not root.left and root.right) or (root.left and not root.right):
            val,size = self.path.pop()
            size += 1
            val2 = (val+root.val)//(size)
            if val2 == root.val: self.count += 1
            self.path[-1][0] = val + root.val
            self.path[-1][1] = size
        else:
            self.path[-3][0] += (self.path[-1][0]+self.path[-2][0])
            self.path[-3][1] += (self.path[-1][1] + self.path[-2][1])
            for _ in range(2):self.path.pop()
            val,size = self.path.pop()
            if (val//(size+1)) == root.val: self.count += 1
            self.path.append([val,size+1])
        return None