# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        result = []
        while temp:
            result.append(temp.val)
            temp = temp.next
        size = len(result)-2
        if size > -2:
            newNode = ListNode(result[size+1])
            temp = newNode
            for index in range(size,-1,-1):
                currNode = ListNode(result[index])
                temp.next = currNode
                temp = temp.next
            return newNode
