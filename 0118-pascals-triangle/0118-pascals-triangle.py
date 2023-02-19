class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lists = []
        for index in range(numRows):
            if lists:
                arr = lists[-1].copy()
                left = 0
                right = 1
                size  = len(arr)
                while right < size:
                    arr[right] = lists[-1][left]+ lists[-1][right]
                    right+= 1
                    left += 1
                arr.append(1)
            else:
                arr = [1]
            lists.append(arr)
        return lists
            