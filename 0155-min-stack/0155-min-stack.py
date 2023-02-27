class MinStack:

    def __init__(self):
        self.stack = []
        self.minm = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minm) > 0:
            if self.minm[-1] >= val:
                self.minm.append(val)
        else:
            self.minm.append(val)
    def pop(self) -> None:
        val = self.stack.pop()
        if self.minm[-1] == val:
            self.minm.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minm[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()