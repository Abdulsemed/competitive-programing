# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.dfs(None,head,1)
        return head
    def dfs(self,before,curr,size):
        if not curr:
            return 
        count = 0
        runner = curr
        while runner and count < size:
            count += 1
            bef = runner
            runner = runner.next
            
        nextHead = runner
        if count % 2 == 0:
            bef = curr
            while curr != nextHead:
                holder = curr.next
                curr.next = runner
                runner = curr
                curr = holder
            before.next = runner
            
        self.dfs(bef,nextHead,size+1)
        
        
        
        