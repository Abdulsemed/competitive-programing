class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dicts = defaultdict(list)
        for index in range(len(groupSizes)):
            dicts[groupSizes[index]].append(index)
        ans = []
        for key in dicts:
            ans.append([])
            for val in dicts[key]:
                if len(ans[-1]) == key:
                    ans.append([])
                ans[-1].append(val)
        return ans
            