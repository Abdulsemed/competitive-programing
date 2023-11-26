# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sums = 0
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            if low <= curr.val <= high:
                sums += curr.val
            if curr.left and curr.val >= low:
                queue.append(curr.left)
            if curr.right and curr.val <= high:
                queue.append(curr.right)
            
        return sums
        