class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        repDict = {}
        repArr = []
        size = len(s)
        for index in range(size):
            repDict[s[index]] = index
        beg = 0
        end = 0
        for index in range(size):
            end = max(end, repDict[s[index]])
            if index == end:
                repArr.append(end - beg +1)
                beg = end+1
                end += 1
        return repArr
                