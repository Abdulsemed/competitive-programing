class Solution:
    def printVertically(self, s: str) -> List[str]:
        verticalList = s.split(" ")
        result = []
        maximum = 0
        size = len(verticalList)
        for element in verticalList:
            maximum = max(len(element), maximum)
        for index in range(maximum):
            lists = []
            for value in range(size):
                if index < len(verticalList[value]):
                    lists.append(verticalList[value][index])
                else:
                    lists.append(" ")
            while lists[-1] == " ":
                lists.pop()
            result.append(''.join(lists))
            
        return result