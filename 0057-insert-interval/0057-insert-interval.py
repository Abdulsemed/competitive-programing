class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newArr = []
        index = 0
        while index < len(intervals):
            if intervals[index][1] >= newInterval[0]:
                if intervals[index][1] > newInterval[1]:
                    if intervals[index][0] > newInterval[1]:
                        newArr.append(newInterval)
                        newArr.append(intervals[index])
                    else:
                        pos = intervals[index][0]
                        if intervals[index][0] > newInterval[0]:
                            pos = newInterval[0]
                        newArr.append([pos, intervals[index][1]])
                    index += 1
                    newInterval = []
                    break
                else:
                    pos = intervals[index][0]
                    if intervals[index][0] > newInterval[0]:
                        pos = newInterval[0]
                    while index < len(intervals) and intervals[index][1] < newInterval[1]:
                        index += 1
                    if index < len(intervals):
                        if intervals[index][0] > newInterval[1]:
                            newArr.append([pos, newInterval[1]])
                        else:
                            newArr.append([pos, intervals[index][1]])
                            index += 1
                    else:
                        newArr.append([pos, newInterval[1]])
                    newInterval = []
                    break
            else:
                newArr.append(intervals[index])
                index += 1
        newArr.extend(intervals[index:])
        if newInterval: newArr.append(newInterval)
                
        return newArr
        