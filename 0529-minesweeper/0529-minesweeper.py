class Solution:
    def __init__(self):
        self.directions = [(1,0),(0,1),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        self.visited = set()
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            self.dfs(click[0],click[1],board)
        return board
    def inbound(self,row,col,grid):
        return 0<= row < len(grid) and 0 <= col < len(grid[0])
    def dfs(self,row,col,board):
        self.visited.add((row,col))
        count = 0
        for row_change, col_change in self.directions:
            new_row = row + row_change
            new_col = col + col_change
            if self.inbound(new_row,new_col,board) and board[new_row][new_col] == "M":
                count += 1
        if count == 0:
            board[row][col] = "B"
            for row_change, col_change in self.directions:
                new_row = row + row_change
                new_col = col + col_change
                if (new_row,new_col) not in self.visited and self.inbound(new_row,new_col,board):
                        self.dfs(new_row,new_col,board)
        else:
            board[row][col] = str(count)
                
                    