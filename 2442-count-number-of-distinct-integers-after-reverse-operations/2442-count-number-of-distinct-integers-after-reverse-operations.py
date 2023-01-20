class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numDict = {}
        for element in nums:
            numDict[element] = 1
        for element in nums:
            val = int(str(element)[::-1])
            numDict[val] =1
        
        print(numDict)
        return len(numDict.values())
            
        