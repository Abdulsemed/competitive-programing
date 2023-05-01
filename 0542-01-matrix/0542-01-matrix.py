class Solution:
    def inbound(self,row,col,mat):
        return 0<= row < len(mat) and 0<= col < len(mat[0])
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rowSize = len(mat)
        colSize = len(mat[0])
        ans = []
        visited = set()
        queue = deque()
        for index in range(rowSize):
            ans.append([])
            for val in range(colSize):
                if mat[index][val] == 0:
                    queue.append((index,val))
                    visited.add((index,val))
                ans[index].append(0)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]        
        while queue:
            length = len(queue)
            for _ in range(length):
                row,col = queue.popleft()
                for row_c,col_c in directions:
                    new_r = row+row_c
                    new_c = col+col_c
                    if self.inbound(new_r,new_c,mat) and (new_r,new_c) not in visited:
                        if mat[new_r][new_c] and ans[new_r][new_c]:
                            queue.append((new_r,new_c))
                            visited.add((new_r,new_c))
                        elif ans[new_r][new_c] == 0:
                            ans[new_r][new_c] = ans[row][col]+1
                            queue.append((new_r,new_c))
                            visited.add((new_r,new_c))
                        else:
                            ans[new_r][new_c] = min(ans[new_r][new_c],ans[row][col]+1)

        return ans
        