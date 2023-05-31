class Solution:
def __init__(self):
self.dicts = defaultdict(int)
self.directions = [(0,1),(1,0)]
def inbound(self,row,col,m,n):
return 0<= row < m and 0<= col <n
def solve(self,row,col,m,n):
if row == m-1 and col == n-1:
return 1
if (row,col) not in self.dicts:
for r,c in self.directions:
new_r = row + r
new_c = col + c
if self.inbound(new_r, new_c,m,n):
self.dicts[(row,col)] += self.solve(new_r,new_c,m,n)
return self.dicts[(row,col)]
def uniquePaths(self, m: int, n: int) -> int:
return self.solve(0,0,m,n)