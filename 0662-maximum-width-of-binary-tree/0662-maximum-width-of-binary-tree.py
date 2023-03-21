# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root,1)])
        maxWidth = 0
        while queue:
            left = queue[0][1]
            right = queue[-1][1]
            maxWidth = max(maxWidth, right-left+1)
            levelQueue = deque()
            while queue:
                node, index = queue.popleft()
                if node.left: levelQueue.append((node.left,index*2))
                if node.right: levelQueue.append((node.right,index*2+1))
            queue= levelQueue
        return maxWidth