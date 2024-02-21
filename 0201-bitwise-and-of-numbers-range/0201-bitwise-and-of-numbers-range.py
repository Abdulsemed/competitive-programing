class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        curr = 2**31
        ans = 0
        while curr:
            if curr & right != 0 and curr & left == 0:
                return ans
            elif curr & right == 0 and curr & left != 0:
                return ans
            elif curr & right != 0 and  curr & left != 0:
                ans += curr
                flag = False
            curr = curr >> 1
        
        return ans
            
        
        
            
                
            