# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        head = dummy
        temp = head
        if temp:
            while temp.next and temp.next.next:
                if temp.next.val == temp.next.next.val:
                    runner = temp.next
                    while runner.next and runner.val == runner.next.val:
                        runner = runner.next
                    temp.next= runner.next
                else:
                    temp = temp.next
        return head.next
                    