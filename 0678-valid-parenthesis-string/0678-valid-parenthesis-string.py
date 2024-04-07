class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for element in s:
            if element != ")":
                stack.append(element)
            else:
                curr = []
                while stack and stack[-1] != "(":
                    val = stack.pop()
                    if val == "*":
                        curr.append(val)
                        
                if not stack and not curr: 
                    return False
                
                if stack:stack.pop()
                else:
                    curr.pop()
                stack += curr
        stac = []
        for element in stack:
            if element != "*":
                stac.append(element)
            elif not stac:
                continue
            else:
                curr = []
                while stac and stac[-1] != "(":
                    stac.pop()
                        
                if not stac: 
                    return False
                stac.pop()       
        if not stac or (stac and stac[0] == "*"):
            return True
        return False