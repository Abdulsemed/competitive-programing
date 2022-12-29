class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        jumpDict = {}
        size = len(words)
        for index in range(size):
            strings = set(words[index])
            sets =''.join(sorted(list(strings)))
            if sets in jumpDict:
                if jumpDict[sets] > 1:
                    jumpDict[sets] -= 1
                    count += jumpDict[sets]
            else:
                jumpDict[sets] = 0
                if index + 1 < size:
                    right = index+1
                    while right < size:
                        if strings == set(words[right]):
                            jumpDict[sets] += 1
                        right += 1
                            
                    count += jumpDict[sets]
                    
        return count