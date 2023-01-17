class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        for index in range(size):
            flag = True
            temp = index
            for val in range(index+1, size):
                if heights[temp] < heights[val]:
                    temp = val
            if temp != index:
                names[index], names[temp] = names[temp], names[index]
                heights[index], heights[temp] = heights[temp], heights[index]
                    
        return names