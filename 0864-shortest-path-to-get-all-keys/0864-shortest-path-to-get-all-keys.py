class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        def inbound (r,c):
            return 0<= r < len(grid) and 0<= c < len(grid[0])
        def low (r,c):
            return  grid[r][c] not in ".,#,@" and grid[r][c].islower()
        keysValue = 0
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if low(row,col):
                    keysValue += (2**count)
                    count += 1
                elif grid[row][col] == "@":
                    start = [row,col]
        queue = deque([start + [0,0]])
        visited = {(0,0,0)}
        ans = float("inf")
        while queue:
            for _ in range(len(queue)):
                # print(queue)
                row,col,mask,moves = queue.popleft()
                
                if mask == keysValue:
                    ans = min(ans,moves)
                for _r,_c in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_r = _r + row
                    new_c = _c + col
                    if inbound(new_r,new_c) and grid[new_r][new_c] != "#":
                        curr = 0
                        if grid[new_r][new_c].isupper():
                            pos = (ord(grid[new_r][new_c].lower()) -97)
                            if (1 << pos) & mask == 0:
                                continue
                        
                        elif low(new_r,new_c) :
                            curr = (ord(grid[new_r][new_c]) - 97)
                            if 1 << curr & mask != 0:
                                curr = 0
                            else:
                                curr = 2**curr
                        if (new_r,new_c,mask+curr) not in visited:
                            queue.append([new_r,new_c,mask+curr,moves+1])
                            visited.add((new_r,new_c,mask+curr))
                            
        if ans != float("inf"):
            return ans
        return -1
                
                    