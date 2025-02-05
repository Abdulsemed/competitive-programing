class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        count = 2
        currSum = 0
        if coins[0] == 1: 
            currSum += 1   
            for index in range(1,len(coins)):
                coins[index-1] = currSum
                currSum += coins[index]
                if currSum - coins[index-1] > count:
                    return count
                if count < currSum:
                    count = currSum
                count += 1

        return currSum+1
        

            
            
            