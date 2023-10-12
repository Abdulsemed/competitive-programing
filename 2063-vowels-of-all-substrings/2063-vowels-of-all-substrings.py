class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        size = len(word)
        sets = {"a", "e", "i", "o", "u"}
        for index in range(size):
            if word[index] in sets:
                count += (size-index) *(index+1)
        
        return count