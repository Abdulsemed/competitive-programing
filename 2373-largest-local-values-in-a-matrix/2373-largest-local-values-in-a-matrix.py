class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        right = 3
        size = len(grid)
        threes = size -2
        maxLists = []
        flag = True
        for index in range(threes):
            maximum = []
            for value in range(size):
                maximum.append(max(grid[value][:right]))
            beg = 0
            for val in range(threes):
                if flag:
                    maxLists.append([max(maximum[beg+val:right+val])])
                else:
                    maxLists[val].append(max(maximum[beg+val:right+val]))
            flag = False
            for value in range(size):
                grid[value].pop(0)
            
        return maxLists