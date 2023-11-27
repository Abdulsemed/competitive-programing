class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*(k)
        self.front = -1
        self.rear = -1
        self.k = k
        self.size = 0
    def enQueue(self, value: int) -> bool: 
        if self.front == -1:
            self.front += 1
        if not self.isFull():
            self.rear += 1
            self.rear = self.rear % self.k
            self.queue[self.rear] = value
            self.size += 1
            return True
        return False
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.front] = 0
            self.front += 1
            self.front = self.front % self.k
            self.size -=1
            return True
        return False
    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.rear]
        return -1
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size >= self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()