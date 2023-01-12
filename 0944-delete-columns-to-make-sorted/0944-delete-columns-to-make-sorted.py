class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        size = len(strs)-1
        innerSize = len(strs[0])
        for row in range(innerSize):
            for col in range(size):
                if strs[col][row] > strs[col+1][row]:
                    count+= 1
                    break
        return count