class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        innerSize = len(matrix[0])
        for index in range(size):
            for val in range (innerSize):
                if matrix[index][val] == 0:
                    for col in range(innerSize):
                        if matrix[index][col] != 0:
                            matrix[index][col] = "*"
                    for row in range(size):
                        if matrix[row][val] != 0:
                            matrix[row][val] = "*"
                        
        for index in range(size):
            for val in range (innerSize):
                if matrix[index][val] == "*":
                    matrix[index][val] = 0