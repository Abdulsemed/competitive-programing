class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for element in words:
            if element == element[::-1]:
                return element
            
        return ""