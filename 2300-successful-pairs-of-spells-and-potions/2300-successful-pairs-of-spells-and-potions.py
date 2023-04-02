class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        count  = []
        potions.sort()
        size = len(potions)
        for index in range(len(spells)):
            left = 0
            right = size-1
            while left <= right:
                mid = left + (right-left)//2
                if potions[mid]*spells[index] >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            count.append(0)
            if -1 < left < size:
                count[-1] = size-left
        return count
        
            
        