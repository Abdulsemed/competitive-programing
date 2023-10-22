import random
class RandomizedSet:

    def __init__(self):
        self.dicts = {}

    def insert(self, val: int) -> bool:
        if self.dicts.get(val,0) == 0:
            self.dicts[val] = 1
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if self.dicts.get(val,0)== 1:
            del self.dicts[val]
            return True
        return False

    def getRandom(self) -> int:
        key = choice(list(self.dicts.keys()))
        return key


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()