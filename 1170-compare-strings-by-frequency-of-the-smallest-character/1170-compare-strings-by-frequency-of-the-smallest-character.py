class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        lists = []
        answer = []
        for element in words:
            dict1 = Counter(list(element))
            val = sorted(dict1.items())
            lists.append(val[0][1])
        # maxim = max(lists)
        minm = min(lists)
        size = len(lists)
        qury = []
        for query in queries:
            dict1 = Counter(list(query))
            val = sorted(dict1.items())
            qury.append(val[0][1])
        lists.sort()
        for query in qury:
            if query < minm:
                answer.append(size)
            else:
                index = 0
                while index < size:
                    if lists[index] > query:
                        break
                    index += 1
                answer.append(size-index)
        
        return answer