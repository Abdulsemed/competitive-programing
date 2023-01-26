class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        repDict = defaultdict(list)
        repArr = []
        repIntervals = []
        size = len(s)
        for index in range(size):
            repDict[s[index]].append(index)
        for key in repDict:
            repIntervals.append([repDict[key][0],repDict[key][-1]])
        beg = 0
        end = 0
        maxSize = 0
        size = len(repIntervals)
        while beg < size:
            end += 1
            maxSize = max(maxSize, repIntervals[beg][1])
            while end < size:
                if maxSize < repIntervals[end][0]:
                    break
                maxSize = max(maxSize, repIntervals[end][1])
                end += 1
            repArr.append(maxSize-repIntervals[beg][0]+1)
            beg = end
        return repArr
                