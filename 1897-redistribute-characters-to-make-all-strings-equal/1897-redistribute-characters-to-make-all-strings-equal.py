class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        word = Counter("".join(words))
        for i,j in word.items():
            if j % len(words) != 0:
                return False
        return True
        
        