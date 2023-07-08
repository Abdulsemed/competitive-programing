from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        newList= SortedList()
        total = 0
        size = len(instructions)
        for val in instructions:
            left_cost = newList.bisect_left(val)
            right_cost = newList.bisect_right(val)
            
            total += min(left_cost, len(newList)- right_cost)
            newList.add(val)
        return total % (10**9 +7)
        