class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row= 0
        col = -1
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        count = 0
        fullSize = len(matrix[0]) * len(matrix)
        lists = []
        while len(lists) < fullSize:
            while col < right:
                col += 1
                lists.append(matrix[row][col])
                count += 1
            if count == fullSize: break
            top += 1
            while row < bottom:
                row += 1
                lists.append(matrix[row][col])
                count += 1
            right -= 1
            if count == fullSize: break
            while col > left:
                col -= 1
                lists.append(matrix[row][col])
                count += 1
            bottom -= 1
            if count == fullSize: break
            while row > top:
                row -= 1
                lists.append(matrix[row][col])
                count += 1
            left += 1
            if count == fullSize: break
            print(row,col)   
        return lists