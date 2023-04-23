# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = -float('inf')

        def gain_from_subtree(node: Optional[TreeNode]) -> int:
            nonlocal maxPath
            if not node:
                return 0
            gain_from_left = max(gain_from_subtree(node.left), 0)
            gain_from_right = max(gain_from_subtree(node.right), 0)
            maxPath = max(maxPath, gain_from_left + gain_from_right + node.val)
            return max(
                gain_from_left + node.val,
                gain_from_right + node.val
            )

        gain_from_subtree(root)
        return maxPath