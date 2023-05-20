class Solution:
    def summaryRanges(self, arr: List[int]) -> List[str]:
        index = 0
        size  = len(arr)
        path = []
        flag = True
        while index < size:
            left = arr[index]
            while index+1 < size and arr[index+1] - arr[index] == 1:
                index += 1
            if arr[index] != left:
                path.append(str(left)+"->"+str(arr[index]))
            else:
                path.append(str(left))
            index += 1
        return path