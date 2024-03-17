class Solution:
    def maxArrayValue(self, arr: List[int]) -> int:
        maxim = arr[-1]
        for index in range(len(arr)-1,0,-1):
            if arr[index] >= arr[index-1]:
                arr[index-1] += arr[index]
            maxim = max(maxim, arr[index-1])
            
        return maxim