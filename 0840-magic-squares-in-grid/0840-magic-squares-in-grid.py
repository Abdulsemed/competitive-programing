class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        size = len(grid)-2
        innerSize = len(grid[0])-2
        count = 0
        for index in range(size):
            for values in range(innerSize):
                diagSumNeg = grid[index][values] + grid[index+1][values+1] + grid[index+2][values+2]
                diagSumPos = grid[index][values+2]+ grid[index+1][values+1] + grid[index+2][values]
                sumCount  = 0
                setUnique = {1,2,3,4,5,6,7,8,9}
                for row in range(index,index+3):
                    colSum= 0
                    rowSum = 0
                    for col in range(values, 3+values):
                        if grid[row][col] in setUnique:
                            setUnique.remove(grid[row][col])
                        else:
                            col = 0
                            break
                        colSum += grid[col+index-values][row-index+values]
                        rowSum +=grid[row][col]
                    if col == 0:
                        break
                    if colSum == rowSum:
                        sumCount += 1
                if sumCount == 3 and diagSumNeg ==diagSumPos and diagSumPos == colSum:
                    count += 1
        return count
                
                