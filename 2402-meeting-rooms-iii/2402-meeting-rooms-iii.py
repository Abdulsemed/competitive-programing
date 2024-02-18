class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        arr = [0]*(n)
        meetings.sort(key = lambda x :(x[0], x[1]))
        heaps = []
        idx = 0
        minim = []
        time = 0
        for i in range(n):
            heapq.heappush(minim,i)  
            
        while idx < len(meetings):
            if heaps:
                time,val = heapq.heappop(heaps)
                heapq.heappush(minim,val)
                
            while heaps and heaps[0][0] == time:
                time,val = heapq.heappop(heaps)
                heapq.heappush(minim,val)
                
            while idx < len(meetings) and len(heaps) < n:
                while heaps and heaps[0][0] <= meetings[idx][0]:
                    time,val = heapq.heappop(heaps)
                    heapq.heappush(minim, val)
                val = heapq.heappop(minim)
                heapq.heappush(heaps, (meetings[idx][1]+max(time-meetings[idx][0],0),val))
                arr[val] += 1
                idx += 1
        maxim = 0
        ans = -1
        for key in range(n):
            if maxim < arr[key]:
                maxim = arr[key]
                ans = key
        return ans
            
                
            