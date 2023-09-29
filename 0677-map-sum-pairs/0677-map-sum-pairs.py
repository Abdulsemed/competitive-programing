class MapSum:

    def __init__(self):
        self.is_end = False
        self.children = [[None,0] for _ in range(26)]
        self.dicts = {}
    def insert(self, key: str, val: int) -> None:
        curr = self
        holder = val
        if key in self.dicts:
            val -= self.dicts[key]
        self.dicts[key] = holder
        
        for letter in key:
            asci = ord(letter) - 97
            if curr.children[asci][0] == None:
                curr.children[asci] = [MapSum(),0 ]
            curr.children[asci][1] += val
            curr = curr.children[asci][0]
        curr.is_end = True

    def sum(self, prefix: str) -> int:
        curr = self
        prev = curr
        for letter in prefix:
            asci = ord(letter) - 97
            if curr.children[asci][0]:
                prev = curr
                curr = curr.children[asci][0]
            else:
                return 0
        return prev.children[ord(prefix[-1])-97][1]

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)