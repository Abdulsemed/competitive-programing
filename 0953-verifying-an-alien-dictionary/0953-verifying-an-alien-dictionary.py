class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        sizeOfChecker = len(words)
        orders = {}
        index = 0
        for elements in order:
            orders[elements] = index
            index += 1
        
        firstWordSize = len(words[0])
        for index in range(len(words)-1):
            secondWordSize = len(words[index+1])
            minSize = min(firstWordSize, secondWordSize)
            for value in range(minSize):
                if orders[words[index][value]] == orders[words[index+1][value]]:
                    pass
                elif orders[words[index][value]] < orders[words[index+1][value]]:
                    break
                else:
                    return False
                if value == minSize-1:
                    if minSize == secondWordSize != firstWordSize:
                        return False
                
            firstWordSize = secondWordSize
            
        return True
                    