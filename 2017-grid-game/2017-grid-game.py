class Solution:
    def choice(self,prefixSum,val):
        colSize = len(prefixSum[0])-1
        if val == 0:
            return prefixSum[1][colSize] - prefixSum[1][1]
        elif val == colSize:
            return prefixSum[2][colSize-1] - prefixSum[1][colSize-1]
        else:
            return max((prefixSum[1][colSize] - prefixSum[1][val]), (prefixSum[2][val-1] - prefixSum[1][val-1]))
        
    def gridSum(self,grid,colSize):
        prefixSum = [[0] *(colSize+1) for _ in range(3)]
        for row in range(2):
            for col in range(colSize):
                prefixSum[row+1][col+1] = grid[row][col] + prefixSum[row+1][col]+prefixSum[row][col+1] - prefixSum[row][col]
        return prefixSum
    
    def gridGame(self, grid: List[List[int]]) -> int:
        colSize = len(grid[0])
        prefixSum = self.gridSum(grid,colSize)
        arr = []
        for col in range(0,colSize+1):
            arr.append(self.choice(prefixSum,col))
        return min(arr)