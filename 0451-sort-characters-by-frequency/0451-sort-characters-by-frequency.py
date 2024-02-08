class Solution:
    def frequencySort(self, s: str) -> str:
        dicts = Counter(s)
        lists = sorted(dicts.items(), key = lambda x:(x[1],x[0]), reverse = True)
        ans = []
        for key,size in lists:
            for _ in range(size):
                ans.append(key)
                
        return "".join(ans)