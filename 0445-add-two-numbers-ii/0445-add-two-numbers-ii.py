# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        l1 = self.reverso(l1)
        l2 = self.reverso(l2)
        temp1 = l1
        temp2 = l2
        remainder = 0
        result = ListNode(None)
        run = result
        while temp1 or temp2 or remainder:
            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0
            Sum = val1+val2+remainder
            run.next = ListNode(Sum%10, None)
            remainder = Sum//10
            run = run.next
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        return self.reverso(result.next)
            
    def reverso(self,head):
        prev = None
        curr = head
        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        return prev
        