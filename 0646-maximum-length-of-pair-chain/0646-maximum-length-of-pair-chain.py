class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:(x[1],x[0]))
        count = 1
        last = pairs[0]
        for index in range(1,len(pairs)):
            if last[1] >= pairs[index][0]:
                if last[1] > pairs[index][1]:
                    last = pairs[index]
            else:
                last = pairs[index]
                count += 1
        return count