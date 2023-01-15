class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        size = len(matrix)
        bottom = size-1
        if len(matrix) == 1:
            return self.innerList(0, matrix, target)
        else:
            while matrix[top][0] <= matrix[bottom][0]:
                mid = (top + bottom) //2
                if matrix[mid][0] == target:
                    return True
                elif matrix[mid][0] < target:
                    if matrix[mid][-1] == target:
                        return True
                    if matrix[mid][-1] > target:
                        return self.innerList(mid, matrix, target)
                    else:
                        top  = mid + 1
                elif matrix[mid][0] > target:
                    bottom = mid -1
                if bottom < 0 or top >= size:
                    break
        return False
    def innerList (self,index, matrix, target):
        top = 0
        innerSize = len(matrix[0])
        bottom = innerSize-1
        if top == bottom:
            if matrix[index][top] == target:
                return True
        else:
            while matrix[index][top] <= matrix[index][bottom]:
              
                mid = (top+bottom)//2
                if matrix[index][mid] == target:
                    return True
                elif matrix[index][mid] > target:
                    bottom = mid -1
                else:
                    top = mid+1
                if bottom < 0 or top >= innerSize:
                    break
        return False 