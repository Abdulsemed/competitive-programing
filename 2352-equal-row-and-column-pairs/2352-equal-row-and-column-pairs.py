class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        pairSet = set()
        pairDict = {}
        size = len(grid)
        for index in range(size):
            tuples = tuple(grid[index])
            pairDict[tuples] = 1 + pairDict.get(tuples, 0)
        for index in range(size):
            pairList = []
            for value in range(size):
                pairList.append(grid[value][index])
            if tuple(pairList) in pairDict:
                count += pairDict[tuple(pairList)]
                
        return count