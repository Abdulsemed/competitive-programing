class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        size = len(grid)
        innerSize = len(grid[0])
        cols  = []
        rows  = []
        for index in range(size):
            rowDict = defaultdict(int)
            for value in range(innerSize):
                rowDict[grid[index][value]] = 1 + rowDict.get(grid[index][value], 0)
            rows.append(rowDict)
        for index in range(innerSize):
            colDict = defaultdict(int)
            for value in range(size):
                colDict[grid[value][index]] = 1 + colDict.get(grid[value][index], 0)
            cols.append(colDict)
        for index in range(size):
            for value in range(innerSize):
                val1 = (rows[index][1] + cols[value][1]) - (rows[index][0]+ cols[value][0])
                grid[index][value] = val1
        return grid