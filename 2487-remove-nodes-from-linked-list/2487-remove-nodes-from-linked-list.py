# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = ListNode(None, head)
        self.dfs(before,before.next)
        return before.next
        
    def dfs(self,before, curr):
        if not curr.next:
            return
        
        self.dfs(curr,curr.next)
        
        if curr.val < curr.next.val:
            before.next = curr.next
        
        
            
        