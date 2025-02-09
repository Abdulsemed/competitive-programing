# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        def further(node,parent):
            if parent and  parent not in dicts:
                dicts[parent] = 0
            if node.left and node.left not in dicts:
                dicts[node.left] = 0
            if node.right and node.right not in dicts:
                dicts[node.right] = 0
            return 
        dicts = {}
        count = 0
        def dfs(node,parent):
            nonlocal count
            if node == None:
                return 

            dfs(node.left,node)
            dfs(node.right, node)

            if node in dicts and dicts[node] == 1:
                further(node,parent)
            if node.left or node.right:
                if not (node.left in dicts or node.right in dicts):
                    # print("1", count)
                    count += 1
                    dicts[node] = 1
                    further(node,parent)
                elif node.left:
                    # print("2", count)
                    
                    if node.left in dicts and dicts[node.left] == 0 and node not in dicts and dicts.get(parent,-1) != 1:
                        dicts[parent] = 1
                        dicts[node] = 0
                        further(parent,None)
                        count += 1
                    elif node.left not in dicts:
                        dicts[node] = 1
                        dicts[node.left] = 0
                        further(node,parent)
                        count += 1
                elif node.right:
                    # print("3", count)
                    
                    if node.right in dicts and dicts[node.right] == 0 and node not in dicts and dicts.get(parent,-1) != 1:
                        dicts[parent] = 1
                        dicts[node] = 0
                        further(parent,None)
                        count += 1
                    elif node.right not in dicts:
                        dicts[node] = 1
                        dicts[node.right] = 0
                        further(node,parent)
                        count += 1
            else:
                # print("here", parent.left in dicts or parent.right in dicts)
                if node == parent:
                    # print("4", count)
                    dicts[node] = 1
                    count += 1
                elif (parent.left in dicts or parent.right in dicts )and dicts.get(parent, 0) == 0:
                    # print("5", count)
                    dicts[parent] = 1
                    dicts[node] = 0
                    further(parent,None)
                    count += 1
        

        dfs(root,root)
        return count

            
        