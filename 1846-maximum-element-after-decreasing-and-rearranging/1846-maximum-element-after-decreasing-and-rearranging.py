class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maxim = -float("inf")
        for index in range(len(arr)):
            if index == 0:
                arr[index] = 1
            elif arr[index] - arr[index-1] > 1:
                arr[index] = arr[index-1]+1
            maxim = max(maxim, arr[index])
        return maxim