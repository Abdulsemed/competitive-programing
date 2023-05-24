class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        arr = sorted([(abs(costs[index][0] - costs[index][1]),index) for index in range(len(costs))], reverse = True)
        a = [0,0]
        b  = [0,0]
        for element,index in arr:
            if element + costs[index][0] == costs[index][1]:
                if a[1] < len(costs)//2:
                    a[0] += costs[index][0]
                    a[1] += 1
                else:
                    b[0] += costs[index][1]
                    b[1] += 1
            elif element + costs[index][1] == costs[index][0]:
                if b[1] < len(costs)//2:
                    b[0] += costs[index][1]
                    b[1] += 1
                else:
                    a[0] += costs[index][0]
                    a[1] += 1
        return a[0]+b[0]