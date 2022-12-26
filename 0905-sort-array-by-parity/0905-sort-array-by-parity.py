class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
    
        sortedNums = []
        for element in nums:
            if element % 2 == 0:
                sortedNums.append(element)
                
        for element in nums:
            if element % 2 != 0:
                sortedNums.append(element)

        return sortedNums