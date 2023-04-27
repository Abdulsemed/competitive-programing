class Solution:
    def __init__(self):
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.visited = set()
        self.bool = False
    def solve(self, board: List[List[str]]) -> None:
        for index in range(len(board)):
            for val in range(len(board[0])):
                curr = set()
                self.bool = True
                if (index,val) not in self.visited and board[index][val] == "O":
                    self.dfs(index,val,board,curr)
                for row,col in curr:
                    if self.bool:
                        board[row][col] = "X"
                    else:
                        board[row][col] = "*"
        for index in range(len(board)):
            for val in range(len(board[0])):
                if board[index][val] == "*": board[index][val] = "O"
        
    def boundary(self,row,col,grid):
        return 0 == row or len(grid)-1 == row or col == 0 or col == len(grid[0])-1
    def inbound(self,row,col,board):
        return  0<= row < len(board) and 0 <= col < len(board[0])
    def dfs(self,row,col,board,curr):
        self.visited.add((row,col))
        curr.add((row,col))
        if self.boundary(row,col,board):
            board[row][col] = "*"
            self.bool = False
        if not self.bool: return
        for row_c, col_c in self.directions:
            new_r = row + row_c
            new_c = col + col_c
            if self.inbound(new_r,new_c,board):
                if board[new_r][new_c] == "O" and (new_r,new_c) not in self.visited:
                    self.dfs(new_r,new_c,board,curr)
                elif board[new_r][new_c] == "*":
                    self.bool = False
            else:
                self.bool = False   
            if not self.bool: return