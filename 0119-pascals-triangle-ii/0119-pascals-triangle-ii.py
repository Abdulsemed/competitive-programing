class Solution:
    def pascal(self,arr,length):
        if length == 0:
            return arr
        arr = self.pascal(arr,length-1)
        if length > 1:
            temp = arr.copy()
            for index in range(1,length):
                arr[index] += temp[index-1]
        arr.append(1)
        return arr
    def getRow(self, rowIndex: int) -> List[int]:
        arr = self.pascal([1],rowIndex)
        return arr