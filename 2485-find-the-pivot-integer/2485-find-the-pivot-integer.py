class Solution:
    def pivotInteger(self, n: int) -> int:
        sums = (n*(n+1))//2
        currSum = 0
        for element in range(1,n+1):
            currSum += element
            if currSum  == (sums+element)-currSum:
                return element
            
        return -1