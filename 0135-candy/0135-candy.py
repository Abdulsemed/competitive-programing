class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        arr = [0]*(len(ratings))
        for index in range(1, len(ratings)):
            if index == 1:
                if ratings[index] > ratings[index-1]:
                    arr[index] = 2
                    arr[index-1] = 1
                elif ratings[index] < ratings[index-1]:
                    arr[index] = 1
                    arr[index-1] = 2
                else:
                    arr[index] = arr[index-1] = 1
                
            elif ratings[index] > ratings[index-1]:
                arr[index] = arr[index-1] + 1
            else:
                arr[index] = 1
                if arr[index-1] == arr[index] and ratings[index-1] > ratings[index]:
                    arr[index-1] = 2
        for index in range(len(ratings)-1,0,-1):
            if ratings[index-1] > ratings[index] and arr[index] >= arr[index-1]:
                arr[index-1] = arr[index] + 1
                
        return sum(arr)