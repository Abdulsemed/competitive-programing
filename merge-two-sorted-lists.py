# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        newNode = ListNode(0)
        runner = newNode
        while temp1 or temp2:
            temp1val = temp1.val if temp1 else 101
            temp2val= temp2.val if temp2 else 101
            if temp1val < temp2val:
                runner.next = ListNode(temp1val)
                temp1 = temp1.next
            else:
                temp2 = temp2.next
                runner.next = ListNode(temp2val)
            runner = runner.next
        return newNode.next