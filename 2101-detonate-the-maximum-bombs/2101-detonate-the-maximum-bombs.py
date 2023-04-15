class Solution:
    def __init__(self):
        self.size = 0
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        count = 0
        self.size = len(bombs)
        for index in range(self.size):
            visited = set()
            self.count = 0
            self.dfs(index, visited,bombs)
            count = max(count, self.count+1)
            if count == self.size:
                break
        
        return count  
    def inBound(row,col):
        return 1<= row and 1<= col
    def dfs(self,index,visited,bombs):
        visited.add(index)
        rad = bombs[index][2]**2
        if self.count == self.size:
            return
        for val in range(self.size):
            check = (bombs[index][0]-bombs[val][0])**2 + (bombs[index][1] - bombs[val][1])**2
            if check <= rad and val not in visited:
                self.count += 1
                self.dfs(val, visited,bombs)
            
                    
            