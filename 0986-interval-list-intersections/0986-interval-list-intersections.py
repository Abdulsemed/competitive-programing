class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        curr = 0
        for index in range(len(firstList)):
            for idx in range(len(secondList)):
                if secondList[idx][0] <= firstList[index][0] <= secondList[idx][1]:
                    ans.append([max(secondList[idx][0], firstList[index][0]),
                                    min(secondList[idx][1], firstList[index][1])
                                   ])
                elif secondList[idx][0] <= firstList[index][1] <= secondList[idx][1]:
                    ans.append([max(secondList[idx][0], firstList[index][0]),
                                    min(secondList[idx][1], firstList[index][1])
                                   ])
                elif firstList[index][0] <= secondList[idx][0] <= firstList[index][1]:
                    ans.append([max(secondList[idx][0], firstList[index][0]),
                                    min(secondList[idx][1], firstList[index][1])
                                   ])
                    
        return ans
        