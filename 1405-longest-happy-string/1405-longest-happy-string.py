class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        dicts = {"a":a,"b":b, "c":c}
        heaps = []
        for key in dicts:
            if dicts[key]:
                heapq.heappush(heaps, (-dicts[key], key))
         
        ans = []
        temp = -1
        while heaps:
            size,ele = heapq.heappop(heaps)
            size += 1
            
            if ans and ele == ans[-1]:
                if temp < 1:
                    temp += 1
                elif not heaps:
                    break
                else:
                    curr = heapq.heappop(heaps)
                    heapq.heappush(heaps, (size-1, ele))
                    size, ele = curr
                    size += 1
                    temp = 0 
                ans.append(ele)
            else:
                temp = 0
                ans.append(ele)
                
            if size:
                heapq.heappush(heaps, (size, ele))
        if heaps and  ans and heaps[0][1] != ans[-1]:
            for index in range(min(2, -heaps[0][0])):
                ans.append(heaps[0][1])
        return  "".join(ans)