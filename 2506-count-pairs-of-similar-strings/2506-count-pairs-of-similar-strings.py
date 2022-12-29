class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        size = len(words)
        for index in range(size-1):
            if index+1 < size:
                right = index+1
                setA = set(words[index])
            while right < size:
                if set(words[right]) == setA:
                    count += 1
                right += 1
        
        return count