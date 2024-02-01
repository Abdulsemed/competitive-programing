class Solution:
    def divideArray(self, arr: List[int], k: int) -> List[List[int]]:
        arr.sort()
        ans = []
        for index in range(0,len(arr),3):
            if arr[index+2] - arr[index] > k:
                return []
            ans.append(arr[index:index+3])
            
        return ans