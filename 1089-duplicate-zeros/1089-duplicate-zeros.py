class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        leftPointer = 0
        sizeOfArr = len(arr)
        while leftPointer < sizeOfArr:
            if arr[leftPointer] is  0:
                arr.insert(leftPointer,0)
                leftPointer += 1
                arr.pop()
            leftPointer += 1
                
                
        