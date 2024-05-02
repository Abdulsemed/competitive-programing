return curr
def popMiddle(self) -> int:
curr = -1
if self.back and len(self.back) >= len(self.front):
curr = self.back.pop()
if self.front and len(self.back) < len(self.front):
self.back.append(self.front.popleft())
elif self.front:
curr = self.front.popleft()
return curr
def popBack(self) -> int:
curr = -1
if self.back:
curr = self.back.popleft()
if self.front and len(self.back) < len(self.front):
self.back.append(self.front.popleft())
elif self.front:
curr = self.front.popleft()
return curr
​
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()