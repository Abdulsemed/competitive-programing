class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for index in range(9):
            setRow = {"1","2","3","4","5","6","7","8","9"}
            setCol = {"1","2","3","4","5","6","7","8","9"}
            for val in range(9):
                if index!= val:
                    if board[index][val] != ".":
                        if board[index][val] in setRow:
                            setRow.remove(board[index][val])
                        else:
                            return False
                    if board[val][index] != ".":
                        if board[val][index] in setCol:
                            setCol.remove(board[val][index])
                        else:
                            return False
                elif board[index][val] != ".":
                    if board[index][val] not in setRow or board[index][val] not in setCol:
                        return False
                    else:
                        setRow.remove(board[index][val])
                        setCol.remove(board[index][val])
        for index in range(0,9,3):
            left = 0
            right = 3
            for _ in range(3):
                boxSet = {"1","2","3","4","5","6","7","8","9"}
                for val in range(index, index+3):
                    for values in range(left, right):
                        if board[val][values] != ".":
                            if board[val][values] in boxSet:
                                boxSet.remove(board[val][values])
                            else:
                                return False
                left += 3
                right+= 3
                    
        return True    