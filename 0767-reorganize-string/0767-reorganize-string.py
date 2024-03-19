class Solution:
    def reorganizeString(self, s: str) -> str:
        dicts = Counter(s)
        items = []
        ans = []
        for key,val in dicts.items():
            heapq.heappush(items, (-val, key))
        while len(items) > 1:
            curr1,key1 = heapq.heappop(items)
            curr2,key2 = heapq.heappop(items)
            curr1 += 1
            curr2 += 1
            ans.append(key1)
            ans.append(key2)
            if curr1:
                heapq.heappush(items, (curr1, key1))
            if curr2:
                heapq.heappush(items, (curr2,key2))
                
        if items:
            if -items[0][0] > 1:
                return ""
            ans += items[0][1]
        
        return "".join(ans)