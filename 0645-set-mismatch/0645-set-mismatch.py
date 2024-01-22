class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        sets = Counter(nums)
        maxim = max(nums)
        ans = [0,0]
        for val in range(1,maxim+2):
            if val in sets and sets[val] > 1:
                ans[0] = val
            elif val not in sets:
                ans[1] = val
            if ans[0] != 0 and ans[1] !=0: break
                
        return ans