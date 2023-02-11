# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        flag = False
        if slow:
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    flag = True
                    break
        if flag:
            slow = head
            while fast.next:
                if fast == slow:
                    return slow
                fast = fast.next
                slow = slow.next
                
                
        return None