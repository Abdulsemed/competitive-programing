class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        right = 1
        size = len(arr)
        maxLen = 0
        if size > 1:
            flag = arr[left] > arr[right]
            while right < size:  
                if flag:
                    if arr[right-1] < arr[right]:
                        left = right-1
                        flag = False
                    elif arr[right-1] == arr[right]:
                        left = right
                    right += 1
                else:
                    if arr[right-1] > arr[right]:
                        left = right-1
                        flag = True
                    elif arr[right-1] == arr[right]:
                        left = right
                    right += 1
                flag = not flag
                maxLen = max(maxLen, right-left)
        else:
            maxLen = 1
        return maxLen