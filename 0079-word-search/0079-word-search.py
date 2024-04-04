class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bound(x,y):
            return 0<= x < len(board[0]) and 0<= y < len(board)
        
        self.index = 0
        def dfs(col,row):
            if self.index >= len(word):
                return self.index == len(word)
            if board[row][col] != word[self.index]:
                return False
            visited.add((row,col))
            self.index += 1
            for _row,_col in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_r = _row + row
                new_c = _col + col
                if self.index == len(word) or (bound(new_c,new_r) and (new_r,new_c) not in visited):
                    if dfs(new_c,new_r):
                        return True
            visited.remove((row,col))
            self.index -= 1        
            
        visited = set()
        for i in range(len(board)):
            for idx in range(len(board[i])):
                if dfs(idx,i):
                    return True
            