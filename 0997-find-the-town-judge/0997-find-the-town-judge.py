class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dicts = defaultdict(set)
        for src,end in trust:
            dicts[src].add(end)
        ans = -1
        for index in range(n):
            if len(dicts[index+1]) ==0:
                if ans == -1:
                    ans = index+1
                else:
                    return -1
        for key in dicts:
            if key != ans and ans not in dicts[key]:
                return -1
                
        return ans
                