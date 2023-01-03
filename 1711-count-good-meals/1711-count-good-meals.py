class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powersOfTwo = set()
        deliciousDict = {}
        count = 0
        mod = 10**9 + 7
        for elements in deliciousness:
            deliciousDict[elements] = 1 + deliciousDict.get(elements, 0)
        
        
        for val in range(22):
            powersOfTwo.add(2**val)
        print(deliciousDict)
        for element in deliciousDict:
            for val in powersOfTwo:
                if val - element in deliciousDict:
                    if val - element == element:
                        count += (deliciousDict[element]*(deliciousDict[element]-1))//2
                    else:
                        count += deliciousDict[element]*deliciousDict[val-element]
                        
            deliciousDict[element] = 0
        
        return count % mod
        
        