# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        queue = deque([root])
        dicts = defaultdict(list)
        while queue:
            curr = queue.popleft()
            if curr.left:
                dicts[curr].append(curr.left)
                dicts[curr.left].append(curr)
                queue.append(curr.left)
            if curr.right:
                dicts[curr].append(curr.right)
                dicts[curr.right].append(curr)
                queue.append(curr.right)
            if curr.val == start:
                start = curr
        queue = deque([start])
        level = 0
        visited = {start.val}
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for element in dicts[curr]:
                    if element.val in visited:
                        continue
                    visited.add(element.val)
                    queue.append(element)
            level += 1
            
        return level-1