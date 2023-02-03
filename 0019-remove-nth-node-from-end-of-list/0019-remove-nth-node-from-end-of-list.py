# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = ListNode(None)
        right.next = head
        head = right
        size = 0
        if not left.next:
            return None
        else:
            while left:
                size+= 1
                left = left.next
            right = head
            n = size - n
            curr = 0
            while curr < n:
                right = right.next
                curr += 1
            right.next = right.next.next
        return head.next
        