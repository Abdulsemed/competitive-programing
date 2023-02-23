class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rowSize = len(matrix)+1
        colSize = len(matrix[0])+1
        self.prefixSum = [([0] *(colSize)).copy() for _ in range(rowSize)]
        for row in range(1,rowSize):
            for col in range(1,colSize):
                self.prefixSum[row][col] = self.prefixSum[row-1][col] + self.prefixSum[row][col-1] + matrix[row-1][col-1] - self.prefixSum[row-1][col-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row2+1][col1] - self.prefixSum[row1][col2+1] + self.prefixSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)