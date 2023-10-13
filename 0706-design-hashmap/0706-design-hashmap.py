class Node:
    def __init__(self,key, val, nex = None):
        self.key = key
        self.val = val
        self.next = nex
class MyHashMap:
    def find(self,key):
        curr = self.root
        last = self.root
        while curr.next and curr.key != key:
            last = curr
            curr = curr.next
        return (curr,last)
    def __init__(self):
        self.root = Node(-1,-1)

    def put(self, key: int, value: int) -> None:
        curr,last = self.find(key)
        if curr.key == key:
            curr.val = value
        else:
            newNode = Node(key,value)
            curr.next = newNode 

    def get(self, key: int) -> int:
        curr,last = self.find(key)
        if curr.key == key:
            return curr.val
        return -1

    def remove(self, key: int) -> None:
        curr,last = self.find(key)
        if curr.key == key:
            last.next = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)