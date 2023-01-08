class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        evenArr = []
        evenSet = set()
        size = len(nums)
        for index in range(size):
            if nums[index] % 2 == 0:
                evenSum += nums[index]
                evenSet.add(index)
                
        for query in queries:
            if query[1] in evenSet:
                evenSum -= nums[query[1]]
                evenSet.remove(query[1])    
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 == 0:
                evenSum += nums[query[1]]
                evenSet.add(query[1])
                
            evenArr.append(evenSum)  
            
        return evenArr    