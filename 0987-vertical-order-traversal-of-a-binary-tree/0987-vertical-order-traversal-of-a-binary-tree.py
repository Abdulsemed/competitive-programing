# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dicts = defaultdict(list)
        self.size = -1
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traverse(root,0,0)
        newList = sorted(self.dicts.items())
        answer = []
        for index,item in newList:
            answer.append([item[0] for item in sorted(item, key = lambda val: (val[1],val[0]))])
        return answer
    def traverse(self,root,row,col):
        if not root:
            return row,col
        self.dicts[col].append((root.val,row))
        self.traverse(root.left,row+1,col-1)
        self.traverse(root.right,row+1,col+1)
        
        