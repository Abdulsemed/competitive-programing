class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        dicts = {}
        for element in barcodes:
            dicts[element] = 1 + dicts.get(element, 0)
        
        heaps = []
        for key in dicts:
            heapq.heappush(heaps,[-dicts[key], key])
        index = 0
        while len(heaps)> 1:
            size1, bar1 = heapq.heappop(heaps)
            size2, bar2 = heapq.heappop(heaps)
            barcodes[index] = bar1
            index += 1
            barcodes[index] = bar2
            index += 1
            size1+= 1
            size2+= 1
            if size1:
                heapq.heappush(heaps,[size1,bar1])
            if size2:
                heapq.heappush(heaps,[size2, bar2])
        if heaps:
            barcodes[index] = heaps[0][1]
        return barcodes            