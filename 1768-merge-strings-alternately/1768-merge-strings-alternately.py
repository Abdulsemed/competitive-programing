class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        remain = 0
        if len(word1) < len(word2):
            maxSize = len(word1)
            remain = 1
        else:
            maxSize = len(word2)
        merged = ""
        for index in range(maxSize):
            merged += word1[index] + word2[index]
            
        if remain == 1:
            merged += word2[maxSize:]
        else:
            merged += word1[maxSize:]
            
        return merged