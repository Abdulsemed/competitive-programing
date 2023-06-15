# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        maxim = - float("inf")
        ans = 1
        level = 1
        while queue:
            length = len(queue)
            sums = 0
            for _ in range(length):
                curr = queue.popleft()
                sums += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if maxim < sums:
                ans = level
                maxim = sums
            level += 1
        return ans