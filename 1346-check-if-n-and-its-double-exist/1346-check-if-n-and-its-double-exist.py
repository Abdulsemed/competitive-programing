class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        sizeOfArr = len(arr)
        for index, element in enumerate(arr):
            if element > -1:
                endPointer = sizeOfArr -1 
            else:
                endPointer = 0
            while endPointer != index:
                doubled = element * 2
                if doubled == arr[endPointer]:
                    return True
                if element > - 1:
                    endPointer -= 1
                else:
                    endPointer += 1
                
        return False