class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index in range(len(matrix[0])):
            left = 0
            right = len(matrix)-1
            while left <= right:
                mid = left + (right-left)//2
                if matrix[mid][index] == target:
                    return True
                elif matrix[mid][index] < target:
                    left = mid + 1
                else:
                    right = mid -1
        return False
        
       