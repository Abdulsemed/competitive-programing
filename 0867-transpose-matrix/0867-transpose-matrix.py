class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = []
        for index in range(len(matrix[0])):
            arr.append([])
            for col in range(len(matrix)):
                arr[-1].append(matrix[col][index])
                
        return arr