class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dicts = {}
        sets = set()
        for src, end in paths:
            if dicts.get(src, []) == []:
                dicts[src] = []
            dicts[src].append(end)
            sets.add(end)
        for key in sets:
            if dicts.get(key, 0) == 0:
                return key
            