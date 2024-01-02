class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dicts = {}
        for element in nums:
            dicts[element] = 1 + dicts.get(element, 0)
        ans = []
        for key in dicts:
            for index in range(dicts[key]):
                if index < len(ans):
                    ans[index].append(key)
                else:
                    ans.append([key])
        return ans