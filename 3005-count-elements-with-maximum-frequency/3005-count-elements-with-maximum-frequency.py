class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dicts = Counter(nums)
        reps = {}
        for element in dicts:
            reps[dicts[element]] = 1 + reps.get(dicts[element], 0)
        maxim = -1
        for key in reps:
            maxim = max(key,maxim)
            
        return reps[maxim] *maxim  
        
        