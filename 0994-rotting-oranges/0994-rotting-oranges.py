class Solution:
    def inbound(self,row,col,grid):
        return 0<= row < len(grid) and 0<= col < len(grid[0])
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        directions  =[(0,1),(1,0),(0,-1),(-1,0)]
        count = 0
        ones = 0
        rowSize = len(grid)
        colSize = len(grid[0])
        for index in range(rowSize):
            for val in range(colSize):
                if grid[index][val] == 2:
                    queue.append((index,val))
                    visited.add((index,val))
                elif grid[index][val] == 1:
                    ones += 1
        while queue:
            length = len(queue)
            flag=  False
            for index in range(length):
                row,col = queue.popleft()
                for row_c, col_c in directions:
                    new_row = row + row_c
                    new_col = col + col_c
                    if self.inbound(new_row,new_col,grid) and (new_row,new_col) not in visited:
                        if grid[new_row][new_col] == 1:
                            ones -= 1
                            grid[new_row][new_col] = 2
                            flag = True
                        visited.add((new_row,new_col))
                        if grid[new_row][new_col] == 2:
                            queue.append((new_row,new_col))
            if flag:count += 1
        if ones > 0:
            count  = -1
        return count