class FrontMiddleBackQueue:

    def __init__(self):
        self.arr = deque([])

    def pushFront(self, val: int) -> None:
        self.arr.appendleft(val)
    def pushMiddle(self, val: int) -> None:
        size = len(self.arr)//2
        for index in range(size, len(self.arr)):
            curr = self.arr[index]
            self.arr[index] = val
            val = curr
        self.arr.append(val)
    def pushBack(self, val: int) -> None:
        self.arr.append(val)
    def popFront(self) -> int:
        if self.arr:
            return self.arr.popleft()
        return -1
    def popMiddle(self) -> int:
        if self.arr:
            size = len(self.arr)//2
            if len(self.arr) % 2  == 0:
                size -= 1
            ans = self.arr[size]
            for index in range(size, len(self.arr)-1):
                self.arr[index] = self.arr[index+1]
            self.arr.pop()
            return ans
        return -1
    def popBack(self) -> int:
        if self.arr:
            return self.arr.pop()
        return -1
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()