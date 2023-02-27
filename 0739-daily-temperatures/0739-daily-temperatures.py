class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minStack = []
        size = len(temperatures)
        result = [0]*(size)
        for index in range(size):
            while minStack and temperatures[minStack[-1]] < temperatures[index]:
                val = minStack.pop()
                result[val] = index - val
            minStack.append(index)
            
        return result