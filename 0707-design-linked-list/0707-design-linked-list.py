class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
    def get(self, index: int) -> int:
        temp =self.head
        count = 0
        while temp:
            if count == index:
                return temp.value
            temp = temp.next
            count += 1
        return -1
    def addAtHead(self, val: int) -> None:
        curr = node(val)
        curr.next = self.head
        self.head= curr
    def addAtTail(self, val: int) -> None:
        curr = node(val)
        temp = self.head
        if temp:
            while temp.next is not None:
                temp = temp.next
            temp.next = curr
        else:
            self.head = curr
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = node(val)
        temp = self.head
        curr = 0
        if index == 0:
            self.addAtHead(val)
        elif temp:
            while temp.next is not None:
                if curr == index-1:
                    break
                curr += 1
                temp = temp.next
            if curr == index-1:
                newNode.next = temp.next
                temp.next = newNode
    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        curr = 0
        if index == 0: 
            if temp.next is not None:
                self.head = temp.next
            else:
                self.head = None
        elif temp:
            while temp.next is not None:
                if curr == index-1:
                    break
                curr += 1
                temp = temp.next
            if curr == index-1:
                if temp.next is not None:
                    temp.next = temp.next.next
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)