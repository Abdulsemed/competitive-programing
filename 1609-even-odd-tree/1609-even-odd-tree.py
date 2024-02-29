# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        queue = deque([root])
        while queue:
            length = len(queue)
            before = float("inf")
            if level % 2 == 0:
                before = -float("inf")
            for _ in range(length):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
                if level % 2 == 0:
                    if curr.val % 2 == 0 or  before >= curr.val:
                        return False
                
                elif level % 2 != 0:
                    if curr.val % 2 !=0 or before <= curr.val:
                        return False
                before = curr.val
            level += 1     
        return True
                