class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        commentDict = defaultdict(list)
        size = len(source)
        index = 0 
        lastPos = 0
        flag = False
        while index < size:
            value  = 0
            innerSize = len(source[index])
            while value < innerSize:
                if flag:
                    if source[index][value] == "*":
                        if value + 1 < innerSize and source[index][value+1] == "/":
                            flag  = False
                            value += 1
                else:
                    if source[index][value] == "/":
                        commentDict[lastPos].append(source[index][value])
                        if value + 1 < innerSize:
                            if source[index][value+1] == "/":
                                commentDict[lastPos].pop()
                                break
                            elif source[index][value+1] == "*":
                                commentDict[lastPos].pop()
                                flag = True
                                value += 1
                    else:
                        commentDict[lastPos].append(source[index][value])
                value += 1
            if not flag:
                lastPos += 1
            index += 1
        code = [''.join(values) for values in commentDict.values() if len(values) > 0 ]
        return code
                
                