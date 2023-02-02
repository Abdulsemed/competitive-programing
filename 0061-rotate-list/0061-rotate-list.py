# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
        if size >0:
            k = k%size
        if k > 0 and size > 0:
            count = 0
            temp = head
            if k+1 == size:
                k = 0
            else:
                k = size - k-1
            while count < k:
                temp = temp.next
                count += 1
            lastNode = temp.next
            temp.next = None
            temp = lastNode
            while temp and temp.next:
                temp = temp.next
            temp.next = head
            head = lastNode
        return head