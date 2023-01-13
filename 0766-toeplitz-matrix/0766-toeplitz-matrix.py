class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = 0
        col = 0
        innerSize = len(matrix[0])-1
        size  = len(matrix)-1
        for index in range(innerSize):
            row = 0
            col =index
            while row < size and col < innerSize:
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
                row += 1
                col += 1
        for index in range(1,size):
            row = index
            col = 0
            while row < size and col < innerSize:
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
                row += 1
                col += 1
                
        return True
            