class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        numbersDict = {}
        for index in range(size):
            if target - numbers[index] in numbersDict:
                return [numbersDict[target-numbers[index]]+1,index+1]
            numbersDict[numbers[index]] = index
                
                