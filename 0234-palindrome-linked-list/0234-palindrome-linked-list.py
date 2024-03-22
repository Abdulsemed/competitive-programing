# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        tempFast = head
        
        while tempFast.next and tempFast.next.next:
            tempFast = tempFast.next.next
            temp = temp.next
            
        runner = head
        before = None
        fastRunner = temp.next
        last = temp.next
        if not tempFast.next:
            last = temp
        
        while runner != last:
            holder = runner.next
            runner.next = before
            before = runner
            runner = holder
  
        runner = before
        while runner:
            if runner.val != fastRunner.val:
                return False
            runner = runner.next
            fastRunner = fastRunner.next
        
        return True
        