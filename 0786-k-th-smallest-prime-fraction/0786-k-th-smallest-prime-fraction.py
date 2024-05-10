class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        newArr = []
        for index in range(len(arr)):
            for val in range(index+1, len(arr)):
                newArr.append([arr[index]/arr[val], [arr[index],arr[val]]])
                
        newArr.sort()
        return newArr[k-1][1]