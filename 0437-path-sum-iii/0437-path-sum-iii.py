# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.currSum = 0
        self.count = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathDict = {0:1}
        self.traverse(root, targetSum, pathDict)
        return self.count
    def traverse(self, root, target, pathDict):
        if not root:
            return 
        self.currSum += root.val
        if self.currSum - target in pathDict:
            self.count += pathDict[self.currSum-target]
        
        curr =  deepcopy(pathDict)
        curr[self.currSum] = 1 + curr.get(self.currSum,0)
        self.traverse(root.left, target, curr)
        self.traverse(root.right, target, curr)
        self.currSum -= root.val
        