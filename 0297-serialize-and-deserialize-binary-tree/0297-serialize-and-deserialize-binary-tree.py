# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        if not root:
            return ""
        def dfs(root):
            if not root:
                ans.append("l")
                return root
            ans.append(str(abs(root.val)))
            ans.append("p" if root.val >= 0 else "n")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "".join(ans)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        index = 0
        holder = []
        while index < len(data):
            val = 0
            if data[index] == "l":
                holder.append(None)
            else:
                while data[index] != "p" and data[index] != "n":
                    val = val * 10 + int(data[index])
                    index += 1
                if data[index] == "n":
                    holder.append(-val)
                else:
                    holder.append(val)
            index += 1
        data = holder
        index = 1
        if holder:
            root = TreeNode(holder[0])
        else:
            return None
        def dfs(node):
            nonlocal index
            if index >= len(holder):
                return None
            if holder[index] != None:
                val = TreeNode(holder[index])
                node.left = val
                index += 1
                dfs(val)
            index += 1
            if holder[index] != None:
                val = TreeNode(holder[index])
                node.right = val
                index += 1
                dfs(val)
        dfs(root)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))