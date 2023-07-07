class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxim = 0
        for sentence in sentences:
            maxim = max(maxim, len(sentence.split(" ")))
            
        return maxim