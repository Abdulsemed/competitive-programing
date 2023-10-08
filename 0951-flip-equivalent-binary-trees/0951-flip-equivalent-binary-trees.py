# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 and root2:
                return False
            elif root1 and not root2:
                return False
            elif root1.val != root2.val:
                return False
            
            flag1 = flag2 = True
            if root1.left:
                if root2.left and root1.left.val == root2.left.val:
                    flag1 = dfs(root1.left, root2.left)
                    flag2 = dfs(root1.right, root2.right)
                elif root2.right and root1.left.val == root2.right.val:
                    flag1 = dfs(root1.left, root2.right)
                    flag2 = dfs(root1.right, root2.left)
                else:
                    return False
                if not(flag1 and flag2):
                    return False
            elif root1.right:
                if root2.right and root1.right.val == root2.right.val:
                    flag1 = dfs(root1.right, root2.right)
                    flag2 = dfs(root1.left, root2.left)
                elif root2.left and root1.right.val == root2.left.val:
                    print(root1.right.val, root2.left.val)
                    flag1 = dfs(root1.right, root2.left)
                    flag2 = dfs(root1.left, root2.right)
                else:
                    return False
                if not(flag1 and flag2):
                    return False
                
            return True
        return dfs(root1,root2)
                