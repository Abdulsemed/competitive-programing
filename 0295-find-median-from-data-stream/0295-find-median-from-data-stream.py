class MedianFinder:
    def __init__(self):
        self.left =[]
        self.right = []
    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left,-num)
        elif not self.right:
            heapq.heappush(self.right,num)
        else:
            if -self.left[0] > self.right[0]:
                val = heapq.heappop(self.right)
                val2 = heapq.heappop(self.left)
                heapq.heappush(self.left,-val)
                heapq.heappush(self.right,-val2)
            
            if num > self.right[0]:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -num)
        if len(self.left) > len(self.right)+1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, -val)
        elif len(self.right) > len(self.left) + 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
            
                    
    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0])/2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()