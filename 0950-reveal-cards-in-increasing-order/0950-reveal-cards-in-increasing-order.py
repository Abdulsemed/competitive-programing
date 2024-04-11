class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        size = len(deck)
        index = 0
        arr = [0]* size
        flag = True
        pos  = 0
        while index < size:
            if arr[pos] == 0:
                if flag:
                    arr[pos] = deck[index]
                    index += 1
                flag = not flag
            pos = (pos + 1) % size
            
        return arr
                
    