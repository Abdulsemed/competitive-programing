# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        maxim = []
        if root:
            queue = deque([root])
            while queue:
                length = len(queue)
                val = -float("inf")
                for _ in range(length):
                    curr = queue.popleft()
                    val = max(val, curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                maxim.append(val)
                
        return maxim