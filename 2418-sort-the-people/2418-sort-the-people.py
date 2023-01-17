class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for index in range(size):
            # flag = True
            for val in range(size -index-1):
                if heights[val] < heights[val+1]:
                    flag = False
                    names[val], names[val+1] = names[val+1], names[val]
                    heights[val+1], heights[val] = heights[val], heights[val+1]
            # if flag:
            #     break
                    
        return names