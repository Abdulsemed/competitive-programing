class Solution:
    def inbound(self,row,col,maze):
        return 0<= row < len(maze) and 0<= col < len(maze[0])
    def border(self,new_r,new_c,maze):
        return (new_r == 0 or new_r == len(maze)-1 or new_c == 0 or new_c == len(maze[0])-1)
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = {(entrance[0],entrance[1])}
        entrance.append(0)
        queue = deque([entrance])
        minim = float("inf")
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            length = len(queue)
            for _ in range(length):
                row,col,count = queue.popleft()
                
                for row_c, col_c in directions:
                    new_r = row + row_c
                    new_c = col + col_c
                    if self.inbound(new_r,new_c,maze) and (new_r,new_c) not in visited:
                        if maze[new_r][new_c] == ".":
                            if self.border(new_r,new_c,maze)and [new_r,new_c,0] != entrance:
                                return count+1
                            queue.append((new_r,new_c,count+1))
                            visited.add((new_r,new_c))
                
        return -1