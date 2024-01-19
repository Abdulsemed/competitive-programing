class Solution:
    def inbound(self, row,col,n):
        return 0 <= row < n and 0<= col < n
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        direction = [(1,-1),(1,0),(1,1)]
        dicts = matrix.copy()
        for index in range(len(matrix)-2,-1,-1):
            for val in range(len(matrix)-1,-1,-1):
                curr = float("inf")
                for _r,_c in direction:
                    new_r = index + _r
                    new_c = val + _c
                    if self.inbound(new_r,new_c,len(matrix)):
                        curr = min(curr, dicts[new_r][new_c])
                dicts[index][val] = curr + matrix[index][val]
                    
        return min(dicts[0])
                
                
            