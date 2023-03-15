# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        runner = head
        if head:
            return self.mergesort(runner)
        return head
    def mergesort(self,head):
        if not head.next:
            return head
        temp = head
        fast = head
        if fast.next:
            while fast.next and fast.next.next:
                temp = temp.next
                fast = fast.next.next
            right = temp.next
        temp.next = None
        lefthead = self.mergesort(head)
        righthead = self.mergesort(right)
        newHead = ListNode(None)
        temp = newHead
        while lefthead or righthead:
            val1 = lefthead.val if lefthead else float("inf")
            val2 = righthead.val if righthead else float("inf")
            if val1 < val2:
                temp.next = ListNode(val1)
                if lefthead: lefthead = lefthead.next
            else:
                temp.next = ListNode(val2)
                if righthead: righthead = righthead.next
            temp = temp.next
        return newHead.next