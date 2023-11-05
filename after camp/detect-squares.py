class DetectSquares:

    def __init__(self):
        self.counter = defaultdict(int)
    def add(self, point: List[int]) -> None:
        self.counter[(point[0],point[1])] += 1
    def count(self, point: List[int]) -> int:
        count = 0
        x = defaultdict(int)
        y = defaultdict(int)
        for dx,dy in self.counter:
            if dx == point[0] and dy != point[1]:
                x[dy] = self.counter[(dx,dy)]
            elif dy == point[1] and dx != point[0]:
                y[dx] = self.counter[(dx,dy)]
                
        for element in x:
            for val in y:
                if abs(element-point[1]) == abs(val-point[0]):
                    count += (self.counter[(val,element)]*x[element]*y[val])
                
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)