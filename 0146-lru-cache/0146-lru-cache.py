class Node:
    def __init__(self,val,nex = None,prev = None):
        self.val = val
        self.next = nex
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.root = Node(-1)
        self.last = Node(-2)

    def get(self, key: int) -> int:
        val = self.cache.get(key,(-1,None))
        if val[0] != -1:
            valsNext = val[1].next
            valsPrev = val[1].prev
            if valsNext:
                valsNext.prev = valsPrev
                valsPrev.next = valsNext
            else:
                valsPrev.next = val[1]
                val[1].prev = valsPrev
            if self.last != val[1]:
                self.last.next = val[1]
                val[1].prev = self.last
            if not self.last:
                self.root.next = val[1]
                val[1].prev = self.root
            val[1].next = None
            self.last = val[1]
        return val[0]
    
    def put(self, key: int, value: int) -> None:
        if self.cache.get(key,(-1,None))[0] != -1:
            self.get(key)
            self.cache[key][0] = value
        else:
            if self.capacity == len(self.cache):
                nextNode = self.root.next
                del self.cache[nextNode.val]
                
                if nextNode.next:
                    nextNode.next.prev = self.root   
                self.root.next = nextNode.next
                
            newNode = Node(key)
            if len(self.cache) == 0:
                self.root.next = newNode
                newNode.prev = self.root
                self.last = newNode
            else:
                newNode.prev = self.last
                self.last.next = newNode
                self.last = newNode
            self.cache[key] = [value, newNode]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)