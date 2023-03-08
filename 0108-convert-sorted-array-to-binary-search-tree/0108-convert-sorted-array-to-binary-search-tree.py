# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        tree = self.construct(nums,left,right)
        return tree
    def construct(self,nums,left,right):
        if left > right:
            return
        mid = left +(right-left)//2
#         give the treeNode the left and the right siblings using the constructor and call the function recursively
        return TreeNode(nums[mid],self.construct(nums,left,mid-1),self.construct(nums,mid+1,right))