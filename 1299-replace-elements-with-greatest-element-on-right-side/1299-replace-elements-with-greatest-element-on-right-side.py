class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[-1]
        for index in range(len(arr)-1,-1, -1):
            if index -1 > -1:
                if temp > arr[index-1]:
                    arr[index-1] = temp
                else:
                    temp, arr[index-1] = arr[index-1], temp
                    
            
                
        arr[-1] = -1
        return arr