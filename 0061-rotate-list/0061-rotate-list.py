# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# implement using the k goes first
#         then new pointer starts till the first pointer reaches
# then the first pointer next becomes head
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            size = 1
            temp = head
            while temp.next:
                temp = temp.next
                size += 1
            temp.next = head
            temp = head
            k = k%size
            curr = 0
            k = size - k - 1
            while curr< k:
                temp = temp.next
                curr += 1
            head = temp.next
            temp.next = None
        return head
        