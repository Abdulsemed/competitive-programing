class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = list(preorder.split(","))
        size = len(preorder)
        if size == 1 and preorder[-1] == "#": return True
        
        for index in range(size):
            if preorder[index] != "#":
                if stack:
                    ele, val = stack.pop()
                    val -= 1
                    if val != 0:
                        stack.append([ele, val])
                stack.append([preorder[index],2])
            else:
                if not stack: return False
                ele, val = stack.pop()
                val -= 1
                if val != 0:
                    stack.append([ele, val])
            if not stack : break
                
        if index == size-1 and not stack:
            return True
        
        return False