# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = None
        runner = head
        while runner:
            holder = runner.next
            runner.next = newHead
            newHead = runner
            runner = holder
            
        return newHead
            