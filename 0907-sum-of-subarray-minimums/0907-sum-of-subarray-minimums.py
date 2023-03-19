class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        minStack = []
        currSum = 0
        for index in range(size+1):
            while minStack and (index == size or arr[minStack[-1]] >= arr[index]):
                val = minStack.pop()
                left = -1 if not minStack else minStack[-1]
                right = index
                reps = (right-val)*(val-left)
                currSum += (arr[val]*reps)
            minStack.append(index)
            
        return currSum % (10**9+7)