class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        innerSize = len(matrix)
        size = innerSize//2
        for index in range(size):
            for val in range(index,innerSize-index-1):
                row = index
                col = val
                theValue = matrix[row][col]
                for _ in range(4):
                    temp = row
                    row2= col
                    col2 = innerSize - temp -1
                    tempValue = matrix[row2][col2]
                    matrix[row2][col2] = theValue
                    theValue = tempValue
                    col = col2
                    row = row2
        