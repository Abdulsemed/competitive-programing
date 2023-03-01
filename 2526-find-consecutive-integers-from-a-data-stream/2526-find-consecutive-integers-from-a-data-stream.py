class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.arr=[0]*k
        self.index = -1
        self.flag = False
        self.pointer = -1
    def consec(self, num: int) -> bool:
        self.index += 1
        self.index = self.index % self.k
        self.pointer -= 1
        if num != self.value:
            self.pointer = self.k-1
        self.arr[self.index] = num
        if self.index == self.k-1:
            self.flag = True
        if self.flag and self.pointer < 0:
            return True
        return False
            
# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)