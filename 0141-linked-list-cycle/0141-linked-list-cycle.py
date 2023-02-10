# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        if slow:
            while fast.next and fast.next.next:
                fast = fast.next.next
                if fast == slow:
                    return True
                elif fast == slow.next:
                    return True
                slow = slow.next
        return False