# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def compare(self,temp1,temp2,runner):
        if not(temp1 or temp2):
            return temp1, temp2, runner
        temp1val = temp1.val if temp1 else 101
        temp2val= temp2.val if temp2 else 101
        if temp1val < temp2val:
            runner.next = ListNode(temp1val)
            temp1 = temp1.next
        else:
            runner.next = ListNode(temp2val)
            temp2 = temp2.next
        runner = runner.next
        while temp1 or temp2:
            temp1, temp2, runner = self.compare(temp1,temp2,runner)
        return temp1, temp2, runner
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(None)
        runner = newHead
        self.compare(list1,list2,runner)
        return newHead.next
        
        