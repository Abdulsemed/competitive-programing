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
        self.flag = False
        self.curr = head
        self.dfs(head)
        return head
    def dfs(self,node):
        
        if not node: return 
        self.dfs(node.next)
        
        if self.flag or self.curr == None:
            self.flag = True
            return
        if self.curr.next == node:
            self.curr.next.next = None
            self.flag = True
            return
        if self.curr == node or not self.curr.next:
            node.next = None
            self.flag = True
            return
        temp = self.curr.next
        self.curr.next = node
        node.next = temp
        self.curr = temp
        