class Solution:
def __init__(self):
self.direction = [(1,-1),(1,0),(1,1)]
self.memo = {}
def inbound(self, row,col,n):
return 0 <= row < n and 0<= col < n
def minFallingPathSum(self, matrix: List[List[int]]) -> int:
minim = float("inf")
for index in range(len(matrix)):
minim = min(minim,self.dfs(0,index,matrix))
return minim
def dfs(self, row,col,matrix):
if row == len(matrix)-1:
return matrix[row][col]
if (row,col) in self.memo:
return self.memo[(row,col)]
curr = float("inf")
for _r, _c in self.direction:
new_r = row + _r
new_c = col + _c
if self.inbound(new_r,new_c,len(matrix)):
curr = min(curr,self.dfs(new_r,new_c,matrix))
self.memo[(row,col)] = curr + matrix[row][col]
return self.memo[(row,col)]