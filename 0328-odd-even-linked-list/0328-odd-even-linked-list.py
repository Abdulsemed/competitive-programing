# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            odd = ListNode(head.val,None)
            oddRunner = odd
        else:
            return head
        
        if head.next and head.next.next:
            even = ListNode(head.next.val,None)
            evenRunner = even
            temp = head
            while temp.next and temp.next.next:
                oddRunner.next = temp
                temp = temp.next
                evenRunner.next = temp
                temp = temp.next
                oddRunner = oddRunner.next
                evenRunner = evenRunner.next
            evenRunner.next = None
            if temp:
                oddRunner.next = temp
                oddRunner = oddRunner.next
            if temp.next:
                evenRunner.next = temp.next
            oddRunner.next = even.next         
            return odd.next
        else:
            return head