class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minLen = float ("inf")
        prefixSum = [0]
        for element in nums:
            prefixSum.append(prefixSum[-1]+ element)
        minQueue = collections.deque()
        for index, value in enumerate(prefixSum):
            while minQueue and value <= prefixSum[minQueue[-1]]:
                minQueue.pop()
                
            while minQueue and value - prefixSum[minQueue[0]] >= k:
                minLen = min (minLen, index - minQueue.popleft())
            minQueue.append(index)
            
        return minLen if minLen != float("inf") else -1