class Solution:
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
arr = []
left = 0
right = 0
size = len(nums1) + len(nums2)
while left < len(nums1) or right <len(nums2):
val1 = nums1[left] if left < len(nums1) else float("inf")
val2 = nums2[right] if right < len(nums2) else float("inf")
if val1 < val2:
left += 1
arr.append(val1)
else:
arr.append(val2)
right += 1
if size % 2 and len(arr) == (size//2) +1:
return arr[-1]
elif size % 2 == 0 and len(arr) == (size//2)+1:
return (arr[-1] + arr[-2]) / 2