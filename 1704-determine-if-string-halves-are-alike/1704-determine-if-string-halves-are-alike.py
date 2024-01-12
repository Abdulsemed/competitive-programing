class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        size = len(s)//2
        left = 0
        right = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        for index in range(size):
            if s[index] in vowels:
                left += 1
            if s[index+size] in vowels:
                right += 1
        
        return left==right