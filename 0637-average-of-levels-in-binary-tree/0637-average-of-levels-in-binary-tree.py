# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        visited = {root}
        queue = deque([[0,root]])
        index = 0
        ans = [[0,0]]
        val = 0
        while queue:
            curr = queue.popleft()
            if curr[0] == index:
                ans[index][0] += 1
                ans[index][1] += curr[1].val
            else:
                ans[index]= ans[index][1]/ans[index][0]
                ans.append([1,curr[1].val])
                index += 1
            val = curr[0]+1
            if curr[1].left:
                queue.append([val,curr[1].left])
            if curr[1].right:
                queue.append([val,curr[1].right])
        ans[-1]= ans[index][1]/ans[index][0]
        return ans