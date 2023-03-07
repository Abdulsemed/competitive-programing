class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        size = len(arr)
        right = size-1
        while left <= right:
            mid = left + (right -left)//2
            if  arr[mid-1] < arr[mid] and arr[mid] > arr[mid+1]:
                return mid
            elif mid > 0 and arr[mid] > arr[mid-1] :
                left = mid + 1
            elif mid < size and arr[mid] > arr[mid+1]:
                right = mid - 1
            else:
                if mid > 0:
                    right = left
                else:
                    left = right
            
                