# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        index = 1
        temp = head
        prev = head
        result = ListNode(None)
        runner = result
        while temp:
            last = temp.next
            if index == k:
                index = 1
                runner.next = self.reverso(prev,last)
                runner = prev
                prev = last
            else:
                index += 1
            temp = last
        return result.next 
        
    def reverso(self, head,last):
        curr = head
        prev = last
        while curr != last:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        runner = prev
        return prev