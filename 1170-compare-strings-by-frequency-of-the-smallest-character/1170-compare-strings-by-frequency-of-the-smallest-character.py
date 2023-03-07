class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        lists = []
        answer = []
        for element in words:
            val = element.count(min(element))
            lists.append(val)
        # maxim = max(lists)
        minm = min(lists)
        size = len(lists)
        lists.sort()
        qury = []
        for query in queries:
            val = query.count(min(query))
            qury.append(val)
            left = 0
            right = size-1
            while left <= right:
                mid = left + (right-left)//2
                if lists[mid] <= val:
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(size-left)
        return answer