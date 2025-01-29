class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        maximumArea = 0
        bl = []
        tr = []
        for index in range(len(bottomLeft)):
            bl.append([index, bottomLeft[index]])
            tr.append(topRight[index])

        bl.sort(key=lambda x:(x[1]))
        for index in range(len(bottomLeft)):
            bottomLeft[index] = bl[index][1]
            topRight[index] = tr[bl[index][0]]
        # print(bottomLeft)
        # print(topRight)
        for index in range(len(bottomLeft)):
            for val in range(index+1, len(bottomLeft)):
                x1 = max(bottomLeft[index][0], bottomLeft[val][0])
                y1 = max(bottomLeft[index][1], bottomLeft[val][1])
                x2 = min(topRight[index][0], topRight[val][0])
                y2 = min(topRight[index][1], topRight[val][1])
                flag = False
                if not (bottomLeft[index][0] <= x1 <= topRight[index][0] and bottomLeft[index][1] <= y1 <= topRight[index][1]):
                    flag = True
                if not(bottomLeft[val][0] <= x1 <= topRight[val][0] and bottomLeft[val][1] <= y1 <= topRight[val][1]):
                    flag = True
                
                if not(bottomLeft[index][0] <= x2 <= topRight[index][0] and bottomLeft[index][1] <= y2 <= topRight[index][1]):
                    flag = True
                
                if not(bottomLeft[val][0] <= x2 <= topRight[val][0] and bottomLeft[val][1] <= y2 <= topRight[val][1]):
                    flag = True

                if flag:
                    continue
                # print(bottomLeft[index], bottomLeft[val])
                
                # print(x1,y1, x2,y2)
                length = min(y2-y1, x2-x1)
                maximumArea = max(maximumArea, length*length)
        
        return maximumArea
