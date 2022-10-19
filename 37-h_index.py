citations.sort(reverse=True)
        result = 0
        for index in range(len(citations)):
            if citations[index] != 0: 
                result = index +1
            if citations[index] <=result:
                if citations[index] > result-1:
                    return citations[index]
                elif citations[index] == 0:
                    return result
                else:
                    return result-1
            elif index == len(citations)-1:
                return result
