class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        index  = 0
        size = len(arr)
        ans = []
        while index < size:
            if arr[index]-1 == index:
                index += 1
            elif arr[index] == arr[arr[index]-1]:
                if arr[index] not in ans:
                    ans.append(arr[index])
                index += 1
            else:
                val = arr[index]-1
                arr[index] , arr[val] = arr[val], arr[index]
                
        return ans