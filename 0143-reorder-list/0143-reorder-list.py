# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next  
            
        if fast == slow: return head
        
        slow = slow.next
        while slow:
            temp = slow.next
            slow.next = None
            stack.append(slow)
            slow = temp
            
        runner = head
        while stack:
            temp = runner.next
            runner.next = stack.pop()
            runner = runner.next
            if runner and runner != temp:
                runner.next = temp
                runner = runner.next
            if not stack:
                runner.next = None
                
        return head