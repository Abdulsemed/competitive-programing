class Solution:
    def __init__(self):
        self.dfs = {}
        self.size = {}
    def inbound(self,row,col,grid):
        return 0<= row < len(grid) and 0<= col < len(grid[0])
    def find(self,node):
        if node != self.dfs[node]:
            self.dfs[node] = self.find(self.dfs[node])
        return self.dfs[node]
    def union(self,node1,node2):
        rep1 = self.find(node1)
        rep2 = self.find(node2)
        if rep1 == rep2:
            return 
        elif self.size[rep1] > self.size[rep2]:
            self.dfs[rep2] = self.dfs[rep1]
            self.size[rep1] += self.size[rep2]
        else:
            self.dfs[rep1] = self.dfs[rep2]
            self.size[rep2] += self.size[rep1]
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        for index in range(len(grid)):
            for val in range(len(grid[index])):
                self.dfs[(index,val)] = (index,val)
                self.size[(index,val)] = 1
        dicts = {
            1:[(0,1),(0,-1)],
            2:[(1,0),(-1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(-1,0),(0,1)]
        }
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                for r, c in dicts[grid[row][col]]:
                    if r < 0 or c < 0:
                        continue
                    new_r = row + r
                    new_c = col + c
                    if self.inbound(new_r,new_c,grid) and (-r,-c) in dicts[grid[new_r][new_c]]:
                        self.union((row,col),(new_r,new_c))
        return self.find((0,0)) == self.find((len(grid)-1,len(grid[0])-1))           
                        