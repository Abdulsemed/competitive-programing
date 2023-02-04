class Solution:
    def isPalindrome(self, s: str) -> bool:
        newArr= []
        for element in s:
            if element.isalnum():
                newArr.append(element.lower())
        if newArr == newArr[::-1]:
            return True
        return False