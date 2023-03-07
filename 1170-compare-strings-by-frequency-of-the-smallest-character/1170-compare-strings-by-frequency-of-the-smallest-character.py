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
        lists.sort()
        qury = []
        for query in queries:
            dict1 = Counter(list(query))
            val = sorted(dict1.items())
            qury.append(val[0][1])
            left = 0
            right = size-1
            while left <= right:
                mid = left + (right-left)//2
                if lists[mid] <= val[0][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(size-left)
        return answer