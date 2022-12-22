class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s2 = s[::-1]
        if s2 == s:
            return True
        else:
            return False