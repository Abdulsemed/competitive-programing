class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        newArr = []
        val = 0
        for index in range(1000):
            if val < len(arr) and arr[val] == index+1:
                val += 1
            else:
                k -= 1
            if k==0:
                return index+1
            
        return 1000+k
            