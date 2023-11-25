class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = 1
        right = maxSum
        while left <= right:
            mid = left + (right-left)//2
            if mid - 1 -index > 0:
                val = - ((mid-1 - index)*(mid-index)//2)
            else:
                val = abs(mid - 1 - index)
            
            leftAdd = ((mid-1) *(mid)//2) + val
            
            if n - mid-index < 0:
                val= - (abs(n-mid-index)*(abs(n-mid-index)+1)//2)
            else:
                val = n - mid-index
            value = (mid*(mid+1)//2) + val + leftAdd
            # print(mid,leftAdd,val,value)
            if value <= maxSum:
                left = mid+1
            else:
                right = mid -1
                
        return right