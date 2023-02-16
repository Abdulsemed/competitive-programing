# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(0,head)
        runner = temp
        while runner.next:
            if runner.next.val == val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return temp.next