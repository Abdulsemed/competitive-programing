class Solution:
    def __init__(self):
        self.dicts = defaultdict(int)
    def solve(self,sums,level,nums,target):
        if sums == target:
            return 1
        if (sums, level) in self.dicts:
            return self.dicts[(sums, level)]
        for element in nums:
            if sums + element <= target:
                self.dicts[(sums, level)] += self.solve(sums+element, level+1, nums,target)
        return self.dicts[(sums, level)]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.solve(0,0,nums,target)
        