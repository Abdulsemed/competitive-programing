class Solution:
def __init__(self):
self.dicts = {}
def solve(self,index,flag,arr,diff,curr):
if index >= len(arr):
return 0
if (index,flag) in self.dicts:
return self.dicts[(index,flag)]
if flag:
count = 0
if arr[index] - curr == diff:
val = 0
val1 = self.solve(index,False,arr,diff,arr[index]) + count
val2 = self.solve(index+1,True,arr,diff,curr)
else:
val1 = self.solve(index+1,True,arr,diff,arr[index])
val2= self.solve(index+1,False,arr,diff,arr[index])
self.dicts[(index,flag)] = max(val1,val2)
return self.dicts[(index,flag)]
def longestSubsequence(self, arr: List[int], difference: int) -> int:
self.solve(0,False,arr,difference,arr[0])
print(self.dicts)
return max(self.dicts.values())+1
class Solution:
def __init__(self):
self.dicts = {}
def solve(self,index,flag,arr,diff,curr):
if index >= len(arr):