class Solution:
    def __init__(self):
        self.sets = set()
    def prime(self, num):
        curr = 2
        while curr * curr <= num:
            while num % curr == 0:
                self.sets.add(curr)
                num = num//curr
            curr += 1
        if num > 1:
            self.sets.add(num)
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        for element in nums:
            self.prime(element)
        
        return len(self.sets)