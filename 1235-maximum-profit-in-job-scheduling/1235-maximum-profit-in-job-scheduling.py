class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        for index in range(len(endTime)):
            endTime[index] = [startTime[index],endTime[index],profit[index]]
        endTime.sort(key = lambda x:(x[0],x[1]))
        dicts = {}
        def dfs(index):
            if index >= len(startTime):
                return 0
            if index in dicts:
                return dicts[index]
            maxim = 0
            value = endTime[index][1]
            profit = endTime[index][2]
            left = index
            right = len(startTime)-1
            while left<= right:
                mid = left + (right-left)//2
                if endTime[mid][0] >= value:
                    right = mid -1
                else:
                    left = mid + 1

            maxim = max(dfs(index+1), dfs(left)+ profit)
            dicts[index] = maxim        
            return maxim
        
        return dfs(0)