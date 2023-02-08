# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        newNode = ListNode(0,ListNode(0))
        runner = newNode
        remainder = 0
        while temp1 and temp2:
            runner = runner.next
            vals = str(temp1.val+temp2.val+remainder)
            if len(vals) > 1:
                runner.val, remainder = int(vals[1]), int(vals[0])
            else:
                runner.val, remainder = int(vals[0]), 0     
            temp1 = temp1.next
            temp2 = temp2.next
            runner.next = ListNode(0)
        while temp1:
            runner = runner.next
            vals = str(temp1.val+remainder)
            if len(vals) > 1:
                runner.val, remainder = int(vals[1]), int(vals[0])
            else:
                runner.val, remainder = int(vals[0]), 0  
            temp1 = temp1.next
            runner.next = ListNode(0)
        while temp2:
            runner = runner.next
            vals = str(temp2.val+remainder)
            if len(vals) > 1:
                runner.val, remainder = int(vals[1]), int(vals[0])
            else:
                runner.val, remainder = int(vals[0]), 0 
            temp2 = temp2.next
            runner.next = ListNode(0)
        if remainder:
            runner.next = ListNode(remainder,None)
        else:
            runner.next = None
        return newNode.next