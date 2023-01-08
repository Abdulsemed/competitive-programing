class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        innerSize = len(mat[0])
        size = len(mat)
        fullSize = size * innerSize
        diagonal = [mat[0][0]]
        flag = True
        rowIndex  = 0
        colIndex = 0
        for index in range(1,fullSize):
            if flag:
                col = 1
                row = -1
            else:
                col = -1
                row = 1
            if colIndex + col == innerSize:
                rowIndex += 1
                flag = False
            elif rowIndex + row == size:
                colIndex += 1
                flag = True
            elif colIndex + col < 0:
                rowIndex += 1
                flag = True
            elif rowIndex + row < 0:
                colIndex += 1
                flag = False
            elif 0 <= colIndex + col <innerSize and 0 <= rowIndex + row < size:
                colIndex += col
                rowIndex += row
            diagonal.append(mat[rowIndex][colIndex])
        return diagonal
        