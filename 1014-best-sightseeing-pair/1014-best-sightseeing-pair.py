class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        arr1 = [values[0]]
        arr2 = []
        for index in range(1,len(values)):
            arr1.append(values[index] + index)
            arr2.append(values[index] - index)
        arr1.pop()
        for index in range(len(values)-3,-1,-1):
            arr2[index] = max(arr2[index], arr2[index+1])
        maxim = - float("inf")
        for index in range(len(values)-1):
            maxim = max(maxim, arr1[index] + arr2[index])
        return maxim