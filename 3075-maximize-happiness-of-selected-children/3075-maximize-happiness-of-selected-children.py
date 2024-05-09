class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        sums = 0
        for index in range(min(k,len(happiness))):
            sums += max(happiness[index]-index, 0)
            
        return sums