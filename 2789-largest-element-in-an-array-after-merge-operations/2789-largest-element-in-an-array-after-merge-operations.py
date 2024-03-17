class Solution:
    def maxArrayValue(self, arr: List[int]) -> int:
        maxim = arr[-1]
        for index in range(len(arr)-1,0,-1):
            if maxim >= arr[index-1]:
                maxim += arr[index-1]
            else:
                maxim = arr[index-1]
            
        return maxim