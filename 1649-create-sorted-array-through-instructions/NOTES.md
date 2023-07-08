class Solution:
def createSortedArray(self, instructions: List[int]) -> int:
size = len(instructions)
for index in range(size):
instructions[index] = (instructions[index], [0,0])
arr = self.mergesort(instructions, 0,len(instructions)-1)
print(arr)
count = 0
for val, price in arr:
count += min(price)
return count
def mergesort(self, arr, left,right):
if left == right:
return [arr[left]]
mid = left + (right-left)//2
leftArr = self.mergesort(arr,left,mid)
rightArr = self.mergesort(arr,mid+1, right)
return self.merger(leftArr,rightArr)
def merger(self,leftArr, rightArr):
l_ptr = 0
r_ptr = 0
leftSize, rightSize = len(leftArr), len(rightArr)
arr = []
while l_ptr < leftSize or r_ptr < rightSize:
val1 = leftArr[l_ptr] if l_ptr < leftSize else (float("inf"),())
val2 = rightArr[r_ptr] if r_ptr < rightSize else (float("inf"),())
if val1[0] <= val2[0]:
arr.append(val1)
l_ptr += 1
else:
arr.append(val2)
arr[-1][1][1] = rightSize - r_ptr
r_ptr += 1
arr[-1][1][0] = len(arr)-1
return arr