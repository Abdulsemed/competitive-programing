class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = 0
        arr =[[0 for index in range(val+1)] for val in range(100)]
        arr[0][0] = poured
        flag = True
        while row < query_row and flag :
            for index in range(row+2):
                val1 = 0
                val2 = 0
                if index < len(arr[row]) and arr[row][index] > 1:
                    val1 = (arr[row][index]-1)/2
                    
                if index -1  >= 0 and arr[row][index-1] > 1:
                    val2 = (arr[row][index-1] -1)/2
                arr[row+1][index] += val1 + val2 
            flag = False
            for index in range(row+1):
                if arr[row][index] > 1:
                    arr[row][index] -= (arr[row][index]-1)
                if arr[row][index] >= 1:
                    flag = True
            
            row += 1
        if arr[query_row][query_glass] > 1:
            return 1
        return arr[query_row][query_glass]
            