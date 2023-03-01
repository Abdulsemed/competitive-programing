class MyCircularDeque:

    def __init__(self, k: int):
        self.deque = deque()
        self.k = k
        self.size = 0
        self.rear = -1
        self.front = -1
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            if self.rear == - 1: self.rear += 1
            self.deque.appendleft(value)
            self.front += 1
            self.front = self.front % self.k
            self.size += 1
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            if self.rear == - 1: self.rear += 1
            self.deque.append(value)
            self.size += 1
            self.front += 1
            self.front = self.front % self.k
            return True
        return False
    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque.popleft()
            self.front -= 1
            self.front = self.front % self.k
            self.size -= 1
            return True
        return False
    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            self.front -= 1
            self.front = self.front % self.k
            self.size -= 1
            return True
        return False
    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.rear]
        return -1
    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        return -1
    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.size == self.k:
            return True
        return False

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()