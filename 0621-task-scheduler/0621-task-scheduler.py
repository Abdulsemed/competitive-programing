class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dicts = Counter(tasks)
        count = sum(dicts.values())
        intervals = 0
        items = []
        for key,val in dicts.items():
            heapq.heappush(items, (-val,key))
        while count:
            curr = 0
            holder = []
            while curr <= n and items:
                val, key = heapq.heappop(items)
                val += 1
                curr += 1
                if val !=0:
                    holder.append((val, key))
                    
            for val, key in holder:
                heapq.heappush(items, (val,key))
                
            count -= curr
            if count == 0:
                intervals += curr
            else:
                intervals += (n+1)
            
        return intervals
                