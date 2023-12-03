from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.dicts = defaultdict(SortedList)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dicts[key].add([timestamp,value])
                       
    def get(self, key: str, timestamp: int) -> str:
        if self.dicts.get(key, []) == []:
            return ""
        else:
            left = 0
            right = len(self.dicts[key])-1
            while left<= right:
                mid = left + (right-left)//2
                if self.dicts[key][mid][0] <= timestamp:
                    left = mid + 1
                else:
                    right =mid - 1
            if self.dicts[key][right][0] <= timestamp:       
                return self.dicts[key][right][1]
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)