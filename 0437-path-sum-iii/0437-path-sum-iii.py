# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathDict = {0:1}
        self.currSum = 0
        self.count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.traverse(root, targetSum)
        return self.count
    def traverse(self, root, target):
        if not root:
            return 
        self.currSum += root.val
        if self.currSum - target in self.pathDict:
            self.count += self.pathDict[self.currSum-target]
        self.pathDict[self.currSum] = 1 + self.pathDict.get(self.currSum,0)
        self.traverse(root.left, target)
        self.traverse(root.right, target)
        if self.pathDict[self.currSum] > 1:
            self.pathDict[self.currSum] -= 1
        else:
            del self.pathDict[self.currSum]
        self.currSum -= root.val
        