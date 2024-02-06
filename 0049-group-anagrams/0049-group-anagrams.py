class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        for index in range(len(strs)):
            strs[index]  = [str(sorted(strs[index])),strs[index]]
            
        dicts = defaultdict(list)
        for val,ans in strs:
            dicts[val].append(ans)
            
        return dicts.values()