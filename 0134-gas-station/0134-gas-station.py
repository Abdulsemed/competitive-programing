class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalSum = 0
        node = -1
        currSum = 0
        for index in range(len(cost)):
            if gas[index] - cost[index] + currSum < 0:
                totalSum += currSum
                currSum = 0
                node = -1
            elif node == -1:
                node = index
            if node != -1:
                currSum += gas[index] - cost[index]
            else:
                totalSum += (gas[index] -cost[index])
                
            
        if currSum + totalSum  >= 0:
            return node
        return -1
            
            
            