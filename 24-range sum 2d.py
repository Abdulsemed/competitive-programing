class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.p_sum = [[matrix[index][0]] for index in range(len(matrix))]
        for index in range(len(matrix)):
            for j in range(len(matrix[index])-1):
                self.p_sum[index].append(self.p_sum[index][j] + matrix[index][j+1])
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        result = 0
        if col1 >0:
            while row2 >= row1: 
                result += self.p_sum[row2][col2] - self.p_sum[row2][col1-1]
                row2 -= 1
        else:
            while row2 >= row1: 
                result += self.p_sum[row2][col2]
                row2 -= 1
        return result
